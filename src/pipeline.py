from load import load_workouts
from metrics import aggregate_by_session

def get_session_data():
    return aggregate_by_session(load_workouts())