from fastapi import FastAPI
from api.generate import router as generate_router


app = FastAPI(
    title="AI Studio Backend"
)


app.include_router(generate_router)


@app.get("/")
def home():

    return {
        "message": "AI Studio Backend is running"
    }
