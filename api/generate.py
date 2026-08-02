from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime


router = APIRouter()


projects = []


class VideoRequest(BaseModel):

    prompt: str
    quality: str
    duration: str
    voice: str
    subtitles: bool



@router.post("/api/generate")
async def generate_video(request: VideoRequest):


    project = {

        "id": len(projects) + 1,

        "prompt": request.prompt,

        "quality": request.quality,

        "duration": request.duration,

        "voice": request.voice,

        "subtitles": request.subtitles,

        "created": str(datetime.now())

    }


    projects.append(project)



    return {

        "status":"success",

        "message":"Video project created",

        "project":project

    }
