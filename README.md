# Fire Detection using YOLO and Ultralytics

This project is a fire detection system that uses YOLO (You Only Look Once) and the Ultralytics library for real‑time fire detection in images and videos.

## Requirements

* Python 3.6 or higher
* [PyTorch](https://pytorch.org/) (with CUDA support for GPU acceleration)
* [Ultralytics YOLO](https://github.com/ultralytics/yolov5)

## Install Dependencies

To get started, install the necessary libraries:

```bash
pip install torch
```

```bash
pip install ultralytics
```

## Clone the Repository

Once the dependencies are installed, clone this repository and navigate into the project folder:

```bash
git clone https://github.com/Marinelio/fire_detection.git
```

```bash
cd fire_detection
```

## Project Structure

```plaintext
fire_detection/
│
├── data/            # Dataset (images/videos for detection)
├── models/          # Pre-trained models and weights
├── utils/           # Helper functions for data processing and visualization
├── fire_detector.py # Main script to run the detection
├── requirements.txt # Project dependencies
└── README.md        # Project overview
```

## How to Use

1. Prepare your data by placing images or videos in the `data/` directory.
2. Run detection on a video:

   ```bash
   python fire_detector.py --source data/video.mp4
   ```
3. Or run detection on an image:

   ```bash
   python fire_detector.py --source data/image.jpg
   ```

## Example Code

<div style="display: flex; gap: 20px;">
  <div style="flex: 1;">
    <pre><code># fire_detector.py
import torch
from ultralytics import YOLO

model = YOLO("yolov5s.pt")  # Load pre-trained model

def detect\_fire(image\_path):
results = model(image\_path)
results.show()
return results.pandas().xywh  # Bounding boxes </code></pre>

  </div>
  <div style="flex: 1;">
    <pre><code># usage_example.py
from fire_detector import detect_fire

image\_path = "data/test\_image.jpg"
results = detect\_fire(image\_path)
print(results) </code></pre>

  </div>
</div>

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
