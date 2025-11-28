import pytest
from utils.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient()


def test_get_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_user(api_client):
    payload = {
        "name": "Mahir",
        "job": "Automation Engineer"
    }

    response = api_client.post("/users", data=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Mahir"


# Negative test case: Attempt to retrieve a non-existing user
def test_get_non_existing_user(api_client):
    response = api_client.get("/users/99999")

    assert response.status_code == 404
