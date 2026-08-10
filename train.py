from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="datasets/car_damage/data.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    name="claimvision_damage"
)

print("Training completed!")