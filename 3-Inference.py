import subprocess

# Run the shell command using subprocess
subprocess.run(["python", "Wav2Lip/inference.py", "--checkpoint_path", "Wav2Lip/checkpoints/wav2lip_gan.pth", "--face", "input/1.mp4", "--audio", "input/1.mp3"])
