import torch
from ultralytics import YOLO

# Optional: Control how many CPU threads Torch uses
torch.set_num_threads(torch.get_num_threads())

# Load your trained model
model = YOLO('best.pt')  # Make sure 'best.pt' is in the same folder or give full path

# Run real-time webcam inference
model.predict(
    source=0,         # 0 = default webcam, or use 1, 2... for other cams
    imgsz=640,        # Resize image to 640x640
    conf=0.6,         # Confidence threshold
    show=True,        # Show live window
    save=False,       # Set to True to save the video
    device='cpu'      # Force CPU usage
)
