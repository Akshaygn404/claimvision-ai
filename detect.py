from ultralytics import YOLO
import cv2


model = YOLO("runs/detect/claimvision_damage/weights/best.pt")


results = model.predict(
    source="sample_car.jpg",
    conf=0.4,
    save=True
)


for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        print(model.names[cls], round(conf, 2))

print("Detection complete! Check runs/detect/predict/")