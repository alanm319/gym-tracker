from fastapi import APIRouter, HTTPException
import pandas as pd
import json

from schemas import MetricPoint, ExerciseMetrics
from data import get_workouts_df

router = APIRouter()

@router.get("/exercises")
def get_exercises():
    df = get_workouts_df()
    return json.loads(df.to_json(orient="records", date_format="iso"))

#TODO error checking
@router.get("/exercises/{name}")
def get_exercise(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    if filtered.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Exercise '{name}' not found"
        )
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
@router.get("/exercises/{name}/best-volume", response_model=list[MetricPoint])
def get_best_volume(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    result = filtered.groupby("start_time")["set_volume"].max()
    result = result.rename("value")
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

#TODO error checking for incorrect exercise name and for reps higher than 37
@router.get("/exercises/{name}/1rm", response_model=list[MetricPoint])
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