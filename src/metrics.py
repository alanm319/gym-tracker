from load import load_workouts
import pandas as pd
# this module takes in the exercises and outputs a df where each row 



def aggregate_by_session(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["exercise_title", "date"]).apply(session_metrics).reset_index()
    

def session_metrics(session_df: pd.DataFrame) -> pd.Series:
    return pd.Series({
        "heaviest_weight_lbs": session_df["weight_lbs"].max(),
        "volume": (session_df["weight_lbs"] * session_df["reps"]).sum(),
        "best_set_volume": (session_df["weight_lbs"] * session_df["reps"]).max(),
        "est_1rm": (session_df["weight_lbs"] / (1.0278 - 0.0278 * session_df["reps"])).max()
    })


