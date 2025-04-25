import torch

from ultralytics import YOLO

torch.set_num_threads(torch.get_num_threads())

model = YOLO('best.pt')
model.predict(source=0, imgsz=640, conf=0.6, save=True, device='cpu')
