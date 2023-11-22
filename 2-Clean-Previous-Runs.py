import shutil
import os

# Directories to clean
directories_to_clean = ['temp', 'results', 'output']

for directory in directories_to_clean:
    # Remove files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    print(f"Previous run files in '{directory}' directory removed.")

