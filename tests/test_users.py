import pytest

from utils.data_loader import load_test_data
from utils.schema_validator import assert_matches_schema

EXISTING_USERS = load_test_data("users.json", "existing_users")
NEW_USERS = load_test_data("users.json", "new_users")
INVALID_USER_IDS = load_test_data("users.json", "invalid_user_ids")


@pytest.mark.smoke
@pytest.mark.schema
def test_get_users_returns_valid_list(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert_matches_schema(response.json(), "user_list.json")


@pytest.mark.regression
def test_get_users_returns_unique_ids(api_client):
    ids = [user["id"] for user in api_client.get("/users").json()]

    assert len(ids) == len(set(ids))


@pytest.mark.regression
@pytest.mark.schema
@pytest.mark.parametrize("user", EXISTING_USERS, ids=lambda u: f"user-{u['id']}")
def test_get_user_by_id(api_client, user):
    response = api_client.get(f"/users/{user['id']}")

    assert response.status_code == 200
    body = response.json()
    assert_matches_schema(body, "user.json")
    assert body["id"] == user["id"]
    assert body["username"] == user["username"]
    assert body["email"] == user["email"]


@pytest.mark.regression
@pytest.mark.parametrize("user", EXISTING_USERS, ids=lambda u: u["username"])
def test_filter_users_by_username(api_client, user):
    response = api_client.get("/users", params={"username": user["username"]})

    assert response.status_code == 200
    results = response.json()
    assert len(results) == 1
    assert results[0]["id"] == user["id"]


@pytest.mark.smoke
@pytest.mark.schema
@pytest.mark.parametrize("payload", NEW_USERS, ids=lambda p: p["name"])
def test_create_user(api_client, payload):
    response = api_client.post("/users", data=payload)

    assert response.status_code == 201
    body = response.json()
    assert_matches_schema(body, "created_user.json")
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]


@pytest.mark.regression
def test_update_user(api_client):
    payload = {"name": "Updated Name", "job": "Senior QA"}

    response = api_client.put("/users/1", data=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"
    assert response.json()["id"] == 1


@pytest.mark.regression
def test_patch_user(api_client):
    response = api_client.patch("/users/1", data={"job": "Test Lead"})

    assert response.status_code == 200
    assert response.json()["job"] == "Test Lead"


@pytest.mark.regression
def test_delete_user(api_client):
    response = api_client.delete("/users/1")

    assert response.status_code == 200


@pytest.mark.negative
@pytest.mark.parametrize("case", INVALID_USER_IDS, ids=lambda c: c["reason"])
def test_get_invalid_user_returns_404(api_client, case):
    response = api_client.get(f"/users/{case['id']}")

    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.negative
def test_unknown_endpoint_returns_404(api_client):
    response = api_client.get("/does-not-exist")

    assert response.status_code == 404


@pytest.mark.negative
def test_filter_with_unknown_username_returns_empty_list(api_client):
    response = api_client.get("/users", params={"username": "no-such-user"})

    assert response.status_code == 200
    assert response.json() == []
