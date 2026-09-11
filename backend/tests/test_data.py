from data import get_workouts_df

def test_get_workouts_df():
    REQUIRED_COLUMNS = [
    "title", "start_time", "exercise_title",
    "set_index", "weight_lbs", "reps"
    ]
    df = get_workouts_df()
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    assert len(missing) == 0