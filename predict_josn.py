from ultralytics import YOLO
import json

model = YOLO("runs/detect/claimvision_damage/weights/best.pt")

def detect_damage(image_path):
    results = model(image_path)

    detections = []

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            detections.append({
                "part": model.names[cls_id],
                "confidence": round(float(box.conf[0]), 3),
                "bbox": box.xyxy[0].tolist()
            })

    return detections

output = detect_damage("sample_car.jpg")

print(json.dumps(output, indent=2))