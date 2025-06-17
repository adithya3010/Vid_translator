# backend/db.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["video_translator"]
collection = db["uploads"]

def log_video(filename: str, language: str):
    collection.insert_one({"filename": filename, "language": language})

def store_metadata(video_name: str, language: str):
    print(f"[DB] Storing metadata: {video_name}, {language}")
    # If you're not using MongoDB yet, this can be just a placeholder