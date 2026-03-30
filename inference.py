# Inference script for YOLOv5 model specializing in weapon detection
import cv2
import torch
import time

def alert():
    print("Alert: Weapon detected!")

# Load the YOLOv5 model
def load_model(weights='yolov5s.pt'):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights)
    return model

# Run inference on video file

def run_inference(video_path, model):
    # Open video file
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        start_time = time.time()
        # Perform inference
        results = model(frame)
        end_time = time.time()
        # Display results
        results.render()
        cv2.imshow('Inference', results.ims[0])
        # Check for detections
        for pred in results.pred[0]:
            if pred[-1] == 0:  # Assuming class 0 is for weapons
                alert()
                break
        # Optimize latency check
        latency = end_time - start_time
        if latency < 0.03:
            print("Latency optimized: {:.2f} ms".format(latency * 1000))
        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_path = 'Gun.mp4'
    model = load_model()
    run_inference(video_path, model)
