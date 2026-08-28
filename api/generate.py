import asyncio
import os
import uuid
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from google import genai
from google.genai import types


router = APIRouter(
    prefix="/api",
    tags=["video"]
)


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = os.getenv(
    "VIDEO_MODEL",
    "veo-3.1-lite-generate-preview"
)

OUTPUT_DIR = Path(
    os.getenv(
        "VIDEO_OUTPUT_DIR",
        "generated_videos"
    )
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


if API_KEY:
    client = genai.Client(
        api_key=API_KEY
    )
else:
    client = None


# ---------------------------------------------------------
# Store generation jobs
# ---------------------------------------------------------

jobs = {}


# ---------------------------------------------------------
# Request
# ---------------------------------------------------------

class GenerateVideoRequest(BaseModel):

    prompt: str = Field(
        ...,
        min_length=3,
        max_length=2000
    )

    aspect_ratio: str = "16:9"

    resolution: str = "720p"


# ---------------------------------------------------------
# Start video generation
# ---------------------------------------------------------

@router.post("/generate")
async def generate_video(
    request: GenerateVideoRequest
):

    if client is None:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured."
        )

    if request.aspect_ratio not in [
        "16:9",
        "9:16"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Invalid aspect ratio."
        )

    if request.resolution not in [
        "720p",
        "1080p"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Invalid resolution."
        )

    job_id = uuid.uuid4().hex

    jobs[job_id] = {
        "id": job_id,
        "status": "queued",
        "message": "Video generation started.",
        "video_url": None
    }

    asyncio.create_task(
        create_video(
            job_id,
            request.prompt,
            request.aspect_ratio,
            request.resolution
        )
    )

    return {
        "success": True,
        "job_id": job_id,
        "status": "queued"
    }


# ---------------------------------------------------------
# Generate video in background
# ---------------------------------------------------------

async def create_video(
    job_id,
    prompt,
    aspect_ratio,
    resolution
):

    try:

        jobs[job_id]["status"] = "generating"

        jobs[job_id]["message"] = (
            "AI is generating your video..."
        )

        operation = client.models.generate_videos(
            model=MODEL,
            prompt=prompt,
            config=types.GenerateVideosConfig(
                aspect_ratio=aspect_ratio,
                resolution=resolution,
                number_of_videos=1
            )
        )

        # Wait for generation
        while not operation.done:

            await asyncio.sleep(10)

            operation = client.operations.get(
                operation
            )

        if getattr(
            operation,
            "error",
            None
        ):

            raise RuntimeError(
                str(operation.error)
            )

        response = operation.response

        generated_videos = getattr(
            response,
            "generated_videos",
            None
        )

        if not generated_videos:
            raise RuntimeError(
                "No video was returned."
            )

        generated_video = (
            generated_videos[0]
        )

        video_file = (
            generated_video.video
        )

        filename = (
            f"{job_id}.mp4"
        )

        output_path = (
            OUTPUT_DIR / filename
        )

        # Download the generated video
        client.files.download(
            file=video_file
        )

        video_file.save(
            str(output_path)
        )

        jobs[job_id]["status"] = (
            "completed"
        )

        jobs[job_id]["message"] = (
            "Your video is ready."
        )

        jobs[job_id]["video_url"] = (
            f"/generated-videos/{filename}"
        )

    except Exception as error:

        jobs[job_id]["status"] = "failed"

        jobs[job_id]["message"] = (
            str(error)
        )


# ---------------------------------------------------------
# Check generation status
# ---------------------------------------------------------

@router.get("/generate/{job_id}")
async def get_generation_status(
    job_id: str
):

    if job_id not in jobs:

        raise HTTPException(
            status_code=404,
            detail="Generation job not found."
        )

    return {
        "success": True,
        **jobs[job_id]
    }
