The python program uses Yolov8 model to classify images into 5 categories: Books, Chairs, Computers, Food, Pens.
Model_training is used to train the model while Model_prediction is used for testing the model.
The model is stored in runs/classify/train/weights/best.pt.
The evaluation of the model is stored in runs/classify/val
The testing dataset contains the training dataset plus 2 new images of each category.
The model is able to achieve 100% accuracy on the testing dataset.

Requirements:

ultralytics library : pip install ultralytics