from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from keras.utils import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
import keras.applications.mobilenet_v2 as mobilenetv2

app = Flask(__name__)

gen_label_map={0: 'biological', 1: 'clothes', 2: 'general', 3: 'glass', 4: 'metal', 5: 'paper', 6: 'plastic', 7: 'shoes', 8: 'trash'}

model = load_model('C:/Users/aakas/Desktop/programs/NNs/model12.h5')
from keras.utils import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input

import wikipedia



#load the image
my_image = load_img('C:/Users/aakas/Desktop/programs/NNs/garbage_classification/clothes/clothes4751.jpg', target_size=(224, 224))

#preprocess the image
my_image = img_to_array(my_image)
my_image = np.expand_dims(my_image, axis=0) 
my_image = preprocess_input(my_image)


#make the prediction
prediction = model.predict(my_image)
prediction=[np.round(x) for x in prediction]
for i in prediction:
    print(gen_label_map[i.argmax()])
    query = gen_label_map[i.argmax()]
    print("According to Wikipedia")
    print(query)


#model.make_predict_function()
"""
def classify(my_image): 
    my_image = img_to_array(my_image)
    my_image = np.expand_dims(my_image, axis=0) 
    my_image = preprocess_input(my_image)


    #make the prediction
    prediction = model.predict(my_image)
    prediction=[np.round(x) for x in prediction]
    for i in prediction:
        print(gen_label_map[i.argmax()])
        query = gen_label_map[i.argmax()]
        print("According to Wikipedia")
        print(query)

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("html/assignment.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "C:/Users/aakas/Desktop/programs/NNs/garbage_classification/clothes/clothes4744.jpg"
		img.save(img_path)

		p = classify(img_path)

	return render_template("html/assignment.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
    """

