from fastapi import FastAPI

from .routers import exercises

app = FastAPI()

app.include_router(exercises.router)

@app.get("/")
def get_root():
    return {
        "name": "workouts API",
        "version": "0.0.1",
        "status": "ok"
        }