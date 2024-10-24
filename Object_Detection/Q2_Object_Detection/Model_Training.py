from ultralytics import YOLO

for i in range(1,5):
    model = YOLO(r"C:\Users\aditp\Desktop\Adit\Python programs\THP\Object_Detection\Q2_Object_Detection\runs\detect\train"+str(i)+r"\weights\best.pt")
    results = model.train(data="Train_data.yaml", imgsz=640, epochs = 10, cls = 4, box = 3, dropout = 0.25, cos_lr = True, patience = 2, warmup_epochs = 3, close_mosaic = 5)

    if i%2==0:
        dataset = "Train"
    else:
        dataset = "Train2"

    with open("Train_data.yaml", "w") as file:
        text = '''path: C:/Users/aditp/Desktop/Adit/Python programs/THP/Object_Detection/Q2_Object_Detection/Data
train: images/''' + dataset + '''
val: images/Val

#Classes
names:
 0: Arm
 1: Head
 2: Leg
 3: Body'''
        file.write(text)
