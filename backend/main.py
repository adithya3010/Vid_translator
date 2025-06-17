from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(BASE_DIR, "..", "static")
templates_path = os.path.join(BASE_DIR, "..", "templates")
upload_path = os.path.join(BASE_DIR, "..", "uploads")

os.makedirs(upload_path, exist_ok=True)

app.mount("/static", StaticFiles(directory=static_path), name="static")
app.mount("/uploads", StaticFiles(directory=upload_path), name="uploads")

templates = Jinja2Templates(directory=templates_path)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload(file: UploadFile = File(...), language: str = Form(...)):
    filename = f"translated_{language.lower()}_{file.filename}"
    save_path = os.path.join(upload_path, filename)

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse({"translated_video_path": f"uploads/{filename}"})
