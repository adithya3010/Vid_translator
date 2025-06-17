# backend/translator.py
import os
from moviepy.editor import VideoFileClip
from gtts import gTTS
from db import store_metadata  # Optional MongoDB logging

def translate_audio(video_path: str, target_language: str) -> str:
    print("🎬 Loading video...")
    video = VideoFileClip(video_path)

    if video.audio is None:
        raise Exception("No audio found in uploaded video!")

    audio_path = "backend/output/temp_audio.mp3"
    print("🔊 Extracting original audio...")
    video.audio.write_audiofile(audio_path)

    print("📝 Simulating translation...")
    # Dummy transcript — replace with real speech recognition logic if needed
    dummy_transcript = "Hello! Welcome to our translated video."

    print("🌐 Converting to", target_language)
    tts = gTTS(dummy_transcript, lang=target_language)
    translated_audio_path = "backend/output/translated.mp3"
    tts.save(translated_audio_path)

    print("✅ Translated audio saved to", translated_audio_path)

    # Optionally log metadata to MongoDB
    try:
        store_metadata(video_path, translated_audio_path, target_language)
    except Exception as e:
        print("⚠ Could not store metadata:", e)

    return translated_audio_path