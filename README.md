 # 🧠 VidTrans - Smart Video Translator

VidTrans is an AI-powered web application that allows users to upload a video, choose a target language, and receive a translated audio-overlaid video in return. It enhances accessibility and breaks down language barriers using speech translation technology.

## 🪄 Problem Statement

With so much content in video form, there's a growing need to translate spoken language into a language that people understand. Traditional translation tools don’t support easy video translation for common users. VidTrans solves this by letting users upload a video and get it back with audio translated to their selected language — all with a simple interface.

## 🚀 Features

- Upload any MP4 video
- Choose from multiple languages (via `gTTS`)
- Extract audio and translate it to target language
- Generate new audio using Google Text-to-Speech
- Merge new audio with original video
- Watch translated video directly in browser
- Built with FastAPI and MoviePy for smooth processing

## 🧰 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** FastAPI (Python)
- **AI/ML:** gTTS (Google Text-to-Speech)
- **Media Tools:** MoviePy
- **Hosting:** Localhost / Render / Replit

## 🛠️ How to Run the Project Locally

### Prerequisites

- Python 3.8+
- `pip` installed
- Git
- ffmpeg installed and added to PATH

### Steps

```bash
# Clone the repository
git clone https://github.com/your-username/vidtrans.git
cd vidtrans

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI backend
cd backend
uvicorn main:app --reload
```

Visit: `http://127.0.0.1:8000/`

## 📁 Folder Structure

```
vidtrans/
├── backend/
│   ├── main.py
│   ├── translator.py
│   └── output/
├── frontend/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   └── output/
└── README.md
```

## 📷 Demo and Screenshots

Demo Link: (https://youtube.com/shorts/JNfDI1z4_SA?si=E5oPz-BsoKTgVIJS)

## 💡 Future Scope

- Subtitles generation
- More voice language support (e.g., ElevenLabs)
- Better audio-video sync

## 📄 License

MIT License
