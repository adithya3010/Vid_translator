# backend/merger.py
import shutil
import os

def merge_audio_video(input_path: str, output_filename: str = "translated_video.mp4") -> str:
    output_path = os.path.join("backend", "output", output_filename)
    shutil.copyfile(input_path, output_path)  # Simulate merge
    return output_path