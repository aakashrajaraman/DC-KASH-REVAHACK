# DC-KASH-REVAHACK
Complete project, dataset, and documentation for Team DC-Kash's submission for REVA Hack 2022.

                                                          SpyTrash

                        Waste Categorization and Management Using Computer Vision & Artificial Intelligence.

Problem Preview: 

Due to widespread inefficiencies and mismanagament of waste in cities, the upsurge in disease, injuury, pests, and unhygenic conditions has become an unavoidable aspect of life. As such, there have been several efforts to fix the issue, but no avail. These problems are due to the big and diverse amount of waste produced by a variety of sources. At this point it is essentiwl to develop a solution that not only provides an efficient network of waste collection and management but also allows citizens to take part in it. This involvement of community proves to be a dynamic method of growth and improvement in waste management. This idea proves to be a efficient solution towads waste classification, disposal and management in smart towns and cities. 

Description of project:

 Exploratory Data Analysis:
 The dataset used has various categories that describe the different types of wastes. This data is used to train the model as well as test it. The dataset is balaced with 9 categories namely, biological, clothes, general or mixed trash, glass, metal, paper, plastic, shoes and miscellaneous trash. These categories help in giving the wide bifurcation of managing them. They are used to train the model. The entries for each categories balanced so as to minimize bias. The samples are also randomized so as to increase prediction accuracy during training and testing.


Using computer vision and a backend CNN model built upon the MobilenetV2 pretrained layer, along with a fully built neural network to classify the type of waste, users can now use their personal devices to scan the waste and rejected materials around them and receive the best information about the course of action they need to take. The service is linked with several APIs to provide additional functionality such as a Wikipedia summary to educate the user, collecting geolocation data from the images that the uses uploads, which not only ensures safety and security of the user's data, but also allows the service to hold this data on the back end and make macro predictions on the larger trends in data. 

Along with this data service provides larger information on the category's flammability, toxicity, reusability, and more, to build a sustainable model for waste management. 
In the future, this service will aim to integrate this technology into IoT devices such as drones and CCTV cameras, along with adding a live input feature through frameworks such as YOLO. This service is designed to be used by both individual users, municipalities, and corporations, connecting a network of users to improve the sustainability of the city/location they live in.

How to Use: Using the front end of the service, created in the app2.py file in the repository, the service will render the first HTML page, which has the user interactive elements. Then, after the user uploads an image to the service and clicks the upload button, they will be redirected to the results page, which has a summary of the category's performance, and the best course of action to take, along with the necessary links and contact information in the results.html page. 

For any testing and improvement, the garbageclassification.ipynb file contains the full construction and testing of the model that is running in the backend. 
Credits: the dataset used for this model was collected through several open source repositories available on kaggle.
