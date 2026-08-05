import pandas as pd

REQUIRED_COLUMNS = [
    "title", "start_time", "exercise_title",
    "set_index", "weight_lbs", "reps"
]

def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise Exception(f"CSV is missing required columns: {missing}")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.drop(columns=["description", "set_type", "superset_id", "exercise_notes", "distance_miles", "duration_seconds", "rpe"], inplace=True)
    df['date'] = pd.to_datetime(df['start_time'], format='%b %d, %Y at %I:%M %p').dt.date
    return df


def load_workouts(path: str = "../data/workouts.csv") -> pd.DataFrame:
    return clean_data(load_csv(path))