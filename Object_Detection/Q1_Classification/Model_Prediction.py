#Import the YOLO library
from ultralytics import YOLO

model_path = r"runs\classify\train\weights\best.pt"

#Load the fine tuned model
model = YOLO(model_path)

#Evaluate the model
#The results are stored in runs/classify/val
model.val()
