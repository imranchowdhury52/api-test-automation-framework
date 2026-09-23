import pytest

from config.config import API_TOKEN


@pytest.mark.auth
@pytest.mark.smoke
def test_bearer_token_is_accepted(bearer_client):
    response = bearer_client.get("/bearer")

    assert response.status_code == 200
    assert response.json() == {"authenticated": True, "token": API_TOKEN}


@pytest.mark.auth
@pytest.mark.negative
def test_missing_bearer_token_is_rejected(auth_client):
    response = auth_client.get("/bearer")

    assert response.status_code == 401


@pytest.mark.auth
@pytest.mark.negative
def test_token_can_be_cleared(bearer_client):
    bearer_client.clear_auth()

    response = bearer_client.get("/bearer")

    assert response.status_code == 401


@pytest.mark.auth
def test_basic_auth_with_valid_credentials(auth_client, basic_auth_credentials):
    user, password = basic_auth_credentials
    auth_client.session.auth = (user, password)

    response = auth_client.get(f"/basic-auth/{user}/{password}")

    assert response.status_code == 200
    assert response.json() == {"authenticated": True, "user": user}


@pytest.mark.auth
@pytest.mark.negative
def test_basic_auth_with_wrong_password(auth_client, basic_auth_credentials):
    user, password = basic_auth_credentials
    auth_client.session.auth = (user, "wrong-password")

    response = auth_client.get(f"/basic-auth/{user}/{password}")

    assert response.status_code == 401
