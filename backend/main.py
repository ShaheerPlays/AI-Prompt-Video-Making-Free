import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.generate import router as generate_router


# Load environment variables
load_dotenv()


# Create FastAPI app
app = FastAPI(
    title="AI Studio Backend",
    description="AI Studio video generation backend",
    version="1.0.0"
)


# Allow the frontend to communicate with the backend
frontend_url = os.getenv(
    "FRONTEND_URL",
    "*"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=(
        [frontend_url]
        if frontend_url != "*"
        else ["*"]
    ),
    allow_credentials=(
        frontend_url != "*"
    ),
    allow_methods=["*"],
    allow_headers=["*"],
)


# Generated videos folder
VIDEO_DIR = Path(
    os.getenv(
        "VIDEO_OUTPUT_DIR",
        "generated_videos"
    )
)

VIDEO_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# Make generated videos accessible
app.mount(
    "/generated-videos",
    StaticFiles(
        directory=str(VIDEO_DIR)
    ),
    name="generated-videos"
)


# Add video-generation API
app.include_router(
    generate_router
)


# Home/health check
@app.get("/")
async def root():
    return {
        "name": "AI Studio Backend",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }
