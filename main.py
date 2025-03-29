import torch
import cv2
from ultralytics import YOLO

torch.set_num_threads(torch.get_num_threads())
cv2.setNumThreads(0)  # Let OpenCV decide optimal threads
model = YOLO('best.pt')
model.predict(source='photo.jpg', imgsz=640, conf=0.6, save=True, device='cpu')
