import pytest
from fastapi.testclient import TestClient
from random import randint
from app.main import app

# Test fixture for the FastAPI test client
# Test client sets up server for testing application. The server runs in the background.
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_when_status_is_ok(client: TestClient):
    # Test the /status endpoint
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "OK"

def test_read_root(client: TestClient):
    # Test the root endpoint
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["Hello"] == "World"

def test_read_item(client: TestClient):
    # Test the /items/{item_id} endpoint
    item_id = 1
    q = "search-term"
    response = client.get(f"/items/{item_id}", params={"q": q})
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == item_id
    assert data["q"] == q

def test_when_charging_station_is_created_in_database(client: TestClient):
    # Test the creation of a new charging station

    station_data = {
        "station_id": randint(1000, 9999),
        "name": f"station_{randint(1000, 9999)}",
        "latitude": randint(-90, 90),
        "longitude": randint(-180, 180),
        "address": f"{randint(80000, 80999)} Munich"
    }
    
    response = client.post("/charging_stations/", json=station_data)
    assert response.status_code == 200
    data = response.json()
    station_id = data["station_id"]
    assert station_id != None
    assert data["name"] == station_data["name"]
    assert data["latitude"] == station_data["latitude"]
    assert data["longitude"] == station_data["longitude"]
    assert data["address"] == station_data["address"]