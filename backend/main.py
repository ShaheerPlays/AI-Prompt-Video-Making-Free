import os

from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.generate import router as generate_router


# ---------------------------------------------------------
# Environment
# ---------------------------------------------------------

load_dotenv()


# ---------------------------------------------------------
# App
# ---------------------------------------------------------

app = FastAPI(
    title="AI Studio Backend",
    description="AI Studio video generation backend",
    version="1.0.0"
)


# ---------------------------------------------------------
# CORS
# ---------------------------------------------------------

frontend_url = os.getenv(
    "FRONTEND_URL",
    "*"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        frontend_url
    ] if frontend_url != "*" else ["*"],
    allow_credentials=(
        frontend_url != "*"
    ),
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# Generated video directory
# ---------------------------------------------------------

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


app.mount(
    "/generated-videos",
    StaticFiles(
        directory=str(VIDEO_DIR)
    ),
    name="generated-videos"
)


# ---------------------------------------------------------
# API routes
# ---------------------------------------------------------

app.include_router(
    generate_router
)


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

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
