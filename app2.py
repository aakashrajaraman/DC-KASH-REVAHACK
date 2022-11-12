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
app = Flask(__name__)
gen_label_map = {0: 'biological', 1: 'clothes', 2: 'general', 3: 'glass', 4: 'metal', 5: 'paper', 6: 'plastic', 7: 'shoes', 8: 'trash'}
model = load_model("C:/Users/aakas/Desktop/programs/NNs/model123.h5")
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
    my_image = img_to_array(my_image)
    my_image = np.expand_dims(my_image, axis=0) 
    my_image = preprocess_input(my_image)
    
    y = model.predict(my_image)
    prediction = model.predict(my_image)
    prediction=[np.round(x) for x in prediction]
    for i in prediction:
        print(gen_label_map[i.argmax()])
        query = gen_label_map[i.argmax()]
    return render_template('index.html', prediction=query)
if __name__ == '__main__':
    app.run(port = 3000, debug=True)