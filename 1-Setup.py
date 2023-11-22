import subprocess
import urllib.request
import os
import shutil

use_existing_env = input("Do you want to use a pre-existing conda environment? (yes/no): ").lower()

if use_existing_env == "yes":
    # Prompt the user to input the environment name
    env_name = input("Enter the name of the conda environment: ")

    # Activate the conda environment
    subprocess.run(["conda", "activate", env_name])

directories_to_remove = [
    "CodeFormer",
    "Wav2Lip",
]
for directory in directories_to_remove:
    if os.path.exists(directory):
        shutil.rmtree(directory)
    else:
        print(f"Directory '{directory}' does not exist.")

# Create directories
os.makedirs("sample_data", exist_ok=True)
os.makedirs("output", exist_ok=True)
os.makedirs("input", exist_ok=True)
os.makedirs("images", exist_ok=True)
os.makedirs("temp", exist_ok=True)
os.makedirs("results", exist_ok=True)

# List of Git repository URLs
repository_urls = [
    "https://github.com/zabique/Wav2Lip.git",
    "https://github.com/sczhou/CodeFormer.git",
]

os.makedirs("Codeformer/results", exist_ok=True)

# Clone Git repositories
for url in repository_urls:
    subprocess.run(["git", "clone", url])

# Install Python packages
subprocess.run(["pip", "install", "wget"])

# Download the pretrained model for Wav2Lip
s3fd_url = "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth"
s3fd_target_path = "Wav2Lip/face_detection/detection/sfd/s3fd.pth"

wav2lip_gan_url = "https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA"
wav2lip_gan_target_path = "Wav2Lip/checkpoints/wav2lip_gan.pth"

# Install CodeFormer's dependencies
subprocess.run(["pip", "install", "https://raw.githubusercontent.com/AwaleSajil/ghc/master/ghc-1.0-py3-none-any.whl"])
subprocess.run(["pip", "install", "-r", "Wav2Lip/requirements.txt"])
subprocess.run(["pip", "install", "-r", "CodeFormer/requirements.txt"])

# Install additional Python packages
subprocess.run(["pip", "install", "-q", "youtube-dl"])
subprocess.run(["pip", "install", "ffmpeg-python"])
subprocess.run(["pip", "install", "librosa==0.9.1"])

# Display messages
from IPython.display import clear_output 
clear_output()
print("\nDone")

# Download CodeFormer's weights and install dependencies
os.chdir("CodeFormer")
subprocess.run(["python", "scripts/download_pretrained_models.py", "facelib"])
subprocess.run(["python", "scripts/download_pretrained_models.py", "CodeFormer"])
subprocess.run(["python", "basicsr/setup.py", "develop"])

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(target_path), exist_ok=True)

# Download the file
urllib.request.urlretrieve(url, target_path)

current_directory = os.getcwd()
# Move up one directory
parent_directory = os.path.dirname(current_directory)
# Change to the parent directory
os.chdir(parent_directory)

print("Put mp3 and mp4 in input folder named 1.mp3 and 1.mp4")
pause