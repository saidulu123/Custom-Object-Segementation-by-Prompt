import torch 
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print("using", device, "device")
import os
import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Define the source video and output directory
source_video = "E:\\My projects\\Object Detection in Videos\\input_videos\\foreground_video.mp4"
output_directory = "E:\\My projects\\Object Detection in Videos\\outputs"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Define the output video path
output_video_path = os.path.join(output_directory, "tracked_video.mp4")

# Open the video source
cap = cv2.VideoCapture(source_video)

# Check if video capture opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file {source_video}")
    exit(1)

# Get the video writer initialized to save the output video
# Try different codecs (XVID, MP4V, H264) if the issue persists
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Check if the video writer initialized successfully
if not out.isOpened():
    print(f"Error: Could not open video writer with path {output_video_path}")
    cap.release()
    exit(1)

# Perform tracking on the video
results = model.track(source=source_video, stream=True, tracker="bytetrack.yaml")

# Loop through each frame and save the result
for r in results:
    frame = r.orig_img  # Get the original image frame
    out.write(frame)  # Write the frame to the output video

# Release the video writer and capture objects
cap.release()
out.release()

print(f"Result video saved in: {output_video_path}")
