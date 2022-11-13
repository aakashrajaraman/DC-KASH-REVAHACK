from flask import Flask, render_template, request
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model
from keras.layers import Lambda
import keras.applications.mobilenet_v2 as mobilenetv2
import numpy as np
import pandas as pd
import exif #API to extract metadata
from exif import Image as im
from geopy.geocoders import Nominatim #geolocation services
import wikipedia #use wikipedia api

app = Flask(__name__)
gen_label_map = {0: 'biological', 1: 'clothes', 2: 'general', 3: 'glass', 4: 'metal', 5: 'paper', 6: 'plastic', 7: 'shoes', 8: 'trash'}
model = load_model("C:/Users/aakas/Desktop/programs/NNs/model123.h5")
info = pd.read_csv("C:/Users/aakas/Desktop/programs/NNs/dict.csv")
@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('index.html')
@app.route('/', methods = ['POST'])
def predict():
    # Get the data from the POST request.
    image = request.files['image']
    # Make prediction using model loaded from disk as per the data.
    image_path = image.filename
    image.save(image_path)
    my_image = load_img(image_path, target_size=(224, 224))
    with open(image_path, 'rb') as src:
        copy = im(src)
    my_image = img_to_array(my_image)
    my_image = np.expand_dims(my_image, axis=0) 
    my_image = preprocess_input(my_image)
    
    y = model.predict(my_image)
    prediction = model.predict(my_image)
    prediction=[np.round(x) for x in prediction]
    for i in prediction:
        print(gen_label_map[i.argmax()])
        query = gen_label_map[i.argmax()]
        prediction = query

        #Features
    flammability = info.loc[info['category'] == query, 'flammability'].item()
    toxicity = info.loc[info['category'] == query, 'toxicity'].item()
    reusability =info.loc[info['category'] == query, 'reusability'].item()
    recyclability =info.loc[info['category'] == query, 'recyclability'].item()
    dispose = info.loc[info['category'] == query, 'best mode of disposal'].item()
    contact = info.loc[info['category'] == query, 'contact'].item()
    visit = info.loc[info['category'] == query, 'Visit'].item()
    if query == 'general':
        query = ''
    if query == 'trash':
        query = ''
    if query == 'clothes':
        query = 'post-consumer'
    if query == 'shoes':
        query = 'post-consumer'
    q2 = query + " Waste"

    wiki = wikipedia.summary(q2, 2)

    #Geolocation Services
    geocoder = Nominatim(user_agent = 'SpyTrash')
    q = "info"
    if copy.has_exif:    
        TheDegreeValue, TheMinuteValue, TheSecondValue = copy.gps_latitude
        TheLatitudeValue=TheDegreeValue+(TheMinuteValue/60)+(TheSecondValue/3600)
        TheDegreeValue, TheMinuteValue, TheSecondValue = copy.gps_longitude
        TheLongitudeValue=TheDegreeValue+(TheMinuteValue/60)+(TheSecondValue/3600)
        coord = (TheLatitudeValue, TheLongitudeValue)
        geolocation= geocoder.reverse(coord)
    else:
        geolocation = "No GPS Data"
    return render_template('results.html', prediction=prediction, geolocation = geolocation, visit = visit, 
        contact = contact, dispose = dispose, recyclability = recyclability, reusability=reusability, toxicity = toxicity,
        flammability = flammability, wiki = wiki)
if __name__ == '__main__':
    app.run(port = 3000, debug=True)