# backend/uploader.py
import os
from fastapi import UploadFile
import shutil

UPLOAD_DIR = "backend/output"

def save_uploaded_video(file: UploadFile) -> str:
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_location