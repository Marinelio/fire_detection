import cv2
import torch
from ultralytics import YOLO

# Load the model
model = YOLO('best.pt')

# Open webcam (device 0)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO inference on the frame
    results = model(frame, imgsz=640, conf=0.6, device='cpu')

    # results is a list with one element per image, we have one image: frame
    result = results[0]

    # Draw boxes and labels on frame
    for box in result.boxes:
        # box.xyxy is a tensor: [x1, y1, x2, y2]
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

        # box.conf is confidence
        conf = box.conf[0].item()

        # box.cls is class index (int)
        cls = int(box.cls[0].item())

        # Get class name from model.names dictionary
        label = model.names[cls] if model.names else str(cls)

        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Label with class name and confidence
        cv2.putText(
            frame,
            f"{label} {conf:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )

    # Show the frame
    cv2.imshow('YOLO Live', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and destroy windows
cap.release()
cv2.destroyAllWindows()
