import os
import subprocess


# Definition related functions
import cv2
import matplotlib.pyplot as plt

def display(img1, img2):
    fig = plt.figure(figsize=(25, 10))
    ax1 = fig.add_subplot(1, 2, 1)
    plt.title('Input', fontsize=16)
    ax1.axis('off')
    ax2 = fig.add_subplot(1, 2, 2)
    plt.title('CodeFormer', fontsize=16)
    ax2.axis('off')
    ax1.imshow(img1)
    ax2.imshow(img2)

def imread(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

# Only repairing the face
#CODEFORMER_FIDELITY = 0.5
#input_path = "images"  # Update this with the correct path
#command = f"python CodeFormer/inference_codeformer.py -w {CODEFORMER_FIDELITY} --has_aligned --input_path {input_path}"
#subprocess.run(command, shell=True)

# Whole Images: overall picture repair
CODEFORMER_FIDELITY = 0.7
input_path = "images"
command = f"python CodeFormer/inference_codeformer.py -w {CODEFORMER_FIDELITY} --input_path {input_path} --bg_upsampler realesrgan"
subprocess.run(command, shell=True)
