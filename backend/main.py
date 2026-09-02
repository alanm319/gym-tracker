from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import exercises

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(exercises.router)

@app.get("/")
def get_root():
    return {
        "name": "workouts API",
        "version": "0.0.1",
        "status": "ok"
        }