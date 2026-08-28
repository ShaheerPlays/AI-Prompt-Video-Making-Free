import asyncio
import os
import uuid
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from google import genai
from google.genai import types


router = APIRouter(prefix="/api", tags=["video"])


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = os.getenv(
    "VIDEO_MODEL",
    "veo-3.1-lite-generate-preview"
)

OUTPUT_DIR = Path(
    os.getenv("VIDEO_OUTPUT_DIR", "generated_videos")
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


if not API_KEY:
    client = None
else:
    client = genai.Client(api_key=API_KEY)


# ---------------------------------------------------------
# In-memory job storage
# ---------------------------------------------------------

jobs = {}


# ---------------------------------------------------------
# Request models
# ---------------------------------------------------------

class GenerateVideoRequest(BaseModel):

    prompt: str = Field(
        ...,
        min_length=3,
        max_length=2000
    )

    aspect_ratio: str = Field(
        default="16:9"
    )

    resolution: str = Field(
        default="720p"
    )


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def validate_options(
    aspect_ratio: str,
    resolution: str
):
    allowed_aspect_ratios = {
        "16:9",
        "9:16"
    }

    allowed_resolutions = {
        "720p",
        "1080p"
    }

    if aspect_ratio not in allowed_aspect_ratios:
        raise HTTPException(
            status_code=400,
            detail="Invalid aspect ratio."
        )

    if resolution not in allowed_resolutions:
        raise HTTPException(
            status_code=400,
            detail="Invalid resolution."
        )


async def run_video_generation(
    job_id: str,
    prompt: str,
    aspect_ratio: str,
    resolution: str
):

    try:

        jobs[job_id]["status"] = "generating"
        jobs[job_id]["message"] = (
            "Video generation has started."
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

        jobs[job_id]["operation_name"] = (
            getattr(operation, "name", None)
        )

        # -------------------------------------------------
        # Poll Google until generation is complete
        # -------------------------------------------------

        while not operation.done:

            jobs[job_id]["message"] = (
                "AI is generating your video..."
            )

            await asyncio.sleep(10)

            operation = client.operations.get(
                operation
            )

        # -------------------------------------------------
        # Check response
        # -------------------------------------------------

        if getattr(operation, "error", None):

            error_message = str(
                operation.error
            )

            jobs[job_id]["status"] = "failed"
            jobs[job_id]["message"] = error_message

            return

        response = operation.response

        if not response:
            raise RuntimeError(
                "The video generation API returned no response."
            )

        generated_videos = (
            getattr(
                response,
                "generated_videos",
                None
            )
        )

        if not generated_videos:
            raise RuntimeError(
                "No generated video was returned."
            )

        generated_video = generated_videos[0]

        video_file = generated_video.video

        # -------------------------------------------------
        # Save MP4
        # -------------------------------------------------

        filename = (
            f"{job_id}.mp4"
        )

        output_path = (
            OUTPUT_DIR / filename
        )

        client.files.download(
            file=video_file
        )

        video_file.save(
            str(output_path)
        )

        # -------------------------------------------------
        # Complete
        # -------------------------------------------------

        jobs[job_id]["status"] = "completed"

        jobs[job_id]["message"] = (
            "Your video is ready."
        )

        jobs[job_id]["filename"] = filename

        jobs[job_id]["video_url"] = (
            f"/generated-videos/{filename}"
        )

    except Exception as exc:

        jobs[job_id]["status"] = "failed"

        jobs[job_id]["message"] = (
            str(exc)
        )


# ---------------------------------------------------------
# Start generation
# ---------------------------------------------------------

@router.post("/generate")
async def generate_video(
    request: GenerateVideoRequest
):

    if client is None:

        raise HTTPException(
            status_code=500,
            detail=(
                "GEMINI_API_KEY is not configured "
                "on the backend."
            )
        )

    validate_options(
        request.aspect_ratio,
        request.resolution
    )

    job_id = uuid.uuid4().hex

    jobs[job_id] = {
        "id": job_id,
        "status": "queued",
        "message": "Video generation is queued.",
        "filename": None,
        "video_url": None,
        "operation_name": None
    }

    asyncio.create_task(
        run_video_generation(
            job_id=job_id,
            prompt=request.prompt,
            aspect_ratio=request.aspect_ratio,
            resolution=request.resolution
        )
    )

    return {
        "success": True,
        "job_id": job_id,
        "status": "queued",
        "message": (
            "Video generation started."
        )
    }


# ---------------------------------------------------------
# Check generation status
# ---------------------------------------------------------

@router.get("/generate/{job_id}")
async def generation_status(
    job_id: str
):

    job = jobs.get(job_id)

    if not job:

        raise HTTPException(
            status_code=404,
            detail="Generation job not found."
        )

    return {
        "success": True,
        **job
    }
