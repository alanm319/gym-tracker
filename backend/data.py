import pandas as pd
from db import engine

def get_workouts_df():
    return pd.read_sql("SELECT * FROM sets", engine)