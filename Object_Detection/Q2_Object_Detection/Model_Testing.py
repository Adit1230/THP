from ultralytics import YOLO

model_path = r"C:\Users\aditp\Desktop\Adit\Python programs\THP\Object_Detection\Q2_Object_Detection\runs\detect\train15\weights\best.pt"

# Load a model
model = YOLO(model_path)

#results = model("path/to/image.jpg")
#results[0].show()

results = model.val(data="Train_data.yaml")
