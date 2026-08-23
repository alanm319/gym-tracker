from fastapi.testclient import TestClient
from ..main import app
from ..routers.exercises import get_workouts_df
from httpx import Response

client = TestClient(app)

def test_get_workouts_df():
    REQUIRED_COLUMNS = [
    "title", "start_time", "exercise_title",
    "set_index", "weight_lbs", "reps"
    ]
    df = get_workouts_df()
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    assert len(missing) == 0

def test_read_root():
    response: Response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_get_heaviest_returns_200():
    response: Response = client.get("/exercises/Bench Press (Barbell)/heaviest")
    assert response.status_code == 200

def test_get_heaviest_returns_expected_shape():
    response: Response = client.get("/exercises/Bench Press (Barbell)/heaviest")
    data = response.json()
    assert isinstance(data, list)
    assert "start_time" in data[0]
    assert "value" in data[0]

def test_get_session_volume_returns_200():
    response: Response = client.get("exercises/Bench Press (Barbell)/session-volume")
    assert response.status_code == 200

def test_get_session_volume_returns_expected_shape():
    response: Response = client.get("exercises/Bench Press (Barbell)/session-volume")
    data = response.json()
    assert "start_time" in data[0]
    assert "value" in data[0]

def test_get_best_volume_returns_200():
    response: Response = client.get("exercises/Bench Press (Barbell)/best-volume")
    assert response.status_code == 200

def test_get_best_volume_returns_expected_shape():
    response: Response = client.get("exercises/Bench Press (Barbell)/best-volume")
    data = response.json()
    assert "start_time" in data[0]
    assert "value" in data[0]

def test_get_1rm_returns_200():
    response: Response = client.get("exercises/Bench Press (Barbell)/session-volume")
    assert response.status_code == 200

def test_get_1rm_returns_expected_shape():
    response: Response = client.get("exercises/Bench Press (Barbell)/session-volume")
    data = response.json()
    assert "start_time" in data[0]
    assert "value" in data[0]

def test_get_metrics_returns_200():
    response: Response = client.get("exercises/Bench Press (Barbell)/metrics")
    assert response.status_code == 200

def test_get_metrics_returns_expected_shape():
    response: Response = client.get("exercises/Bench Press (Barbell)/metrics")
    data = response.json()
    assert "start_time" in data[0]
    assert "heaviest" in data[0]
    assert "session_volume" in data[0]
    assert "best_volume" in data[0]
    assert "estimated_1rm" in data[0]