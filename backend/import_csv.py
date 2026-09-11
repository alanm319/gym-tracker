import pandas as pd
from db import engine

df = pd.read_csv("workouts.csv")
df["start_time"] = pd.to_datetime(df["start_time"], format="%b %d, %Y at %I:%M %p")
df["end_time"] = pd.to_datetime(df["end_time"], format="%b %d, %Y at %I:%M %p")
df["set_volume"] = df["weight_lbs"] * df["reps"]
df.to_sql("sets", engine, if_exists="replace", index=False)