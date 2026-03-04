from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_address():

    payload = {
        "name": "Home",
        "street": "MG Road",
        "city": "Bangalore",
        "latitude": 12.9716,
        "longitude": 77.5946
    }

    response = client.post("/addresses", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "Home"
    assert data["city"] == "Bangalore"
    assert "id" in data


def test_update_address():

    payload = {
        "name": "Office",
        "street": "Brigade Road",
        "city": "Bangalore",
        "latitude": 12.972,
        "longitude": 77.595
    }

    create = client.post("/addresses", json=payload)
    address_id = create.json()["id"]

    update_payload = {
        "name": "Office Updated",
        "street": "Brigade Road",
        "city": "Bangalore",
        "latitude": 12.972,
        "longitude": 77.595
    }

    response = client.put(f"/addresses/{address_id}", json=update_payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Office Updated"


def test_delete_address():

    payload = {
        "name": "Temp",
        "street": "Test Street",
        "city": "Test City",
        "latitude": 10.0,
        "longitude": 20.0
    }

    create = client.post("/addresses", json=payload)
    address_id = create.json()["id"]

    response = client.delete(f"/addresses/{address_id}")

    assert response.status_code == 204


def test_nearby_addresses():

    payload = {
        "name": "Nearby Place",
        "street": "Test Street",
        "city": "Test City",
        "latitude": 12.9716,
        "longitude": 77.5946
    }

    client.post("/addresses", json=payload)

    response = client.get(
        "/addresses/nearby?lat=12.9716&lon=77.5946&distance_km=5"
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)