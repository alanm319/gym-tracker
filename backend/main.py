from fastapi import FastAPI
import pandas as pd
import json

def get_workouts_df():
    df = pd.read_csv("workouts.csv")
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])
    df["set_volume"] = df["weight_lbs"] * df["reps"]
    return df

app = FastAPI()

@app.get("/")
def get_root():
    return {"Hello": "World"}

@app.get("/exercises")
def get_exercises():
    df = get_workouts_df()
    return json.loads(df.to_json(orient="records", date_format="iso"))

#TODO error checking
@app.get("/exercises/{name}")
def get_exercise(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    return json.loads(filtered.to_json(orient="records", date_format="iso"))

#TODO error checking
@app.get("/exercises/{name}/heaviest")
def get_heaviest(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    result = filtered.groupby("start_time")["weight_lbs"].max()
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

#TODO error checking
@app.get("/exercises/{name}/session-volume")
def get_session_volume(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    result = filtered.groupby("start_time")["set_volume"].sum()
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

#TODO error checking
@app.get("/exercises/{name}/best-volume")
def get_best_volume(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    result = filtered.groupby("start_time")["set_volume"].max()
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

#TODO error checking for incorrect exercise name and for reps higher than 37
@app.get("/exercises/{name}/1rm")
def get_1rm(name: str):
    df = get_workouts_df()
    filtered = df[df["exercise_title"] == name]
    filtered["estimated_1rm"] = filtered["weight_lbs"] / (1.0278 - 0.0278 * filtered["reps"])
    result = filtered.groupby("start_time")["estimated_1rm"].max()
    return json.loads(result.reset_index().to_json(orient="records", date_format="iso"))

@app.get("/exercise-names")
def get_exercise_names():
    df = get_workouts_df()
    return df["exercise_title"].unique().tolist()