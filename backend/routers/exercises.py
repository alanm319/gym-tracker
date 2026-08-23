from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import json

router = APIRouter()

class MetricPoint(BaseModel):
    start_time: str
    value: float
    
class ExerciseMetrics(BaseModel):
    start_time: str
    heaviest: float
    session_volume: float
    best_volume: float
    estimated_1rm: float

def get_workouts_df():
    df = pd.read_csv("workouts.csv")
    df["start_time"] = pd.to_datetime(df["start_time"], format="%b %d, %Y at %I:%M %p",)
    df["end_time"] = pd.to_datetime(df["end_time"], format="%b %d, %Y at %I:%M %p",)
    df["set_volume"] = df["weight_lbs"] * df["reps"]
    return df

@router.get("/exercises/")
def get_exercises():
    df = get_workouts_df()
    return json.loads(df.to_json(orient="records", date_format="iso"))

#TODO error checking
@router.get("/exercises/{name}")
def get_exercise(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    return json.loads(filtered.to_json(orient="records", date_format="iso"))

#TODO error checking
@router.get("/exercises/{name}/heaviest", response_model=list[MetricPoint])
def get_heaviest(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    result = filtered.groupby("start_time")["weight_lbs"].max()
    result = result.rename("value")
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

#TODO error checking
@router.get("/exercises/{name}/session-volume", response_model=list[MetricPoint])
def get_session_volume(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    result = filtered.groupby("start_time")["set_volume"].sum()
    result = result.rename("value")
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

#TODO error checking
@router.get("/exercises/{name}/best-volume")
def get_best_volume(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    result = filtered.groupby("start_time")["set_volume"].max()
    result = result.rename("value")
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

#TODO error checking for incorrect exercise name and for reps higher than 37
@router.get("/exercises/{name}/1rm")
def get_1rm(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name].copy()
    filtered["estimated_1rm"] = filtered["weight_lbs"] / (1.0278 - 0.0278 * filtered["reps"])
    result = filtered.groupby("start_time")["estimated_1rm"].max()
    result = result.rename("value")
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

@router.get("/exercises/{name}/metrics", response_model=list[ExerciseMetrics])
def get_metrics(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name].copy()
    filtered["estimated_1rm"] = filtered["weight_lbs"] / (1.0278 - 0.0278 * filtered["reps"])
    result = filtered.groupby("start_time").agg(
        heaviest = ("weight_lbs", "max"),
        session_volume = ("set_volume", "sum"),
        best_volume = ("set_volume", "max"),
        estimated_1rm = ("estimated_1rm", "max")
    )
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

@router.get("/exercise-names")
def get_exercise_names():
    df = get_workouts_df()
    return df["exercise_title"].unique().tolist()