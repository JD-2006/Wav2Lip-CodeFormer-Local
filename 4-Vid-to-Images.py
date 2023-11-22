import cv2
from tqdm import tqdm
import os

# Assuming 'images' is a subdirectory of the script's location
output_directory = os.path.join(os.path.dirname(__file__), 'images')

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

video_path = "results/result_voice.mp4"
vidcap = cv2.VideoCapture(video_path)

number_of_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidcap.get(cv2.CAP_PROP_FPS)
print(f"FPS: {fps}, Frames: {number_of_frames}")

for frame_number in tqdm(range(number_of_frames)):
    _, image = vidcap.read()
    output_path = os.path.join(output_directory, f"{frame_number:04d}.jpg")
    cv2.imwrite(output_path, image)
