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
