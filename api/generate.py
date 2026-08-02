from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class VideoRequest(BaseModel):

    prompt: str
    quality: str
    duration: str
    voice: str
    subtitles: bool



@router.post("/api/generate")
async def generate_video(request: VideoRequest):

    return {

        "status": "success",

        "message": "Video generation request received",

        "video": {

            "prompt": request.prompt,

            "quality": request.quality,

            "duration": request.duration,

            "voice": request.voice,

            "subtitles": request.subtitles

        }

    }
