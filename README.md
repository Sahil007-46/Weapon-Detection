# Weapon Detection

## Installation

To set up the YOLOv5 inference environment, follow these steps:

1. Clone the YOLOv5 repository:
   ```bash
   git clone https://github.com/ultralytics/yolov5
   cd yolov5
   ```

2. Install required packages:
   ```bash
   pip install -U -r requirements.txt
   ```

3. Download the trained model weights:
   You can download weights for various models from the [YOLOv5 releases](https://github.com/ultralytics/yolov5/releases). Place the weights in the yolov5 directory.

## Usage

To run inference on an image using YOLOv5, use the following command:
```bash
python inference.py --weights yolov5s.pt --source path/to/your/image.jpg
```
Replace `yolov5s.pt` with the weight file you downloaded and `path/to/your/image.jpg` with your input image path.
