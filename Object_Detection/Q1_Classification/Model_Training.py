# import YOLO library
from ultralytics import YOLO

yolo_model = "yolov8s-cls.pt"
data_path = "Data"

# Load a pretrained model
model = YOLO(yolo_model)

# Fine tune the model
model.train(data = data_path, epochs = 25, warmup_epochs = 0)
