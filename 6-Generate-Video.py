import os
import cv2
import ffmpeg
from tqdm import tqdm
import numpy as np

restored_frames_path = 'results/images_0.7/final_results/'
processed_video_output_path = 'output'

dir_list = os.listdir(restored_frames_path)
dir_list.sort()

batch = 0
batch_size = 600

for i in tqdm(range(0, len(dir_list), batch_size)):
    img_array = []
    start, end = i, i + batch_size
    print("processing ", start, end)
    for filename in tqdm(dir_list[start:end]):
        file_path = os.path.join(restored_frames_path, filename)
        img = cv2.imread(file_path)
        if img is None:
            continue
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(processed_video_output_path+'/batch_'+str(batch).zfill(4)+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
    batch = batch + 1

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

# Audio and video merging to generate the final audio video
audio_input_path = ffmpeg.input('input/1.mp3')
video_input_pattern = ffmpeg.input('output/batch_0000.avi')

print("Consolidating audio and video")

# Combine audio and video
out = ffmpeg.output(video_input_pattern, audio_input_path, 'output/final.mp4')

# Run the command
out.run()

print("Congratulations, the audio and video merger is completed, stored in output/final.mp4")

