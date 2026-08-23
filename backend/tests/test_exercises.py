from fastapi.testclient import TestClient
from main import app
from httpx import Response

client = TestClient(app)


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