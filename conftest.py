import pytest

from config.config import (
    API_TOKEN,
    AUTH_BASE_URL,
    BASIC_AUTH_PASSWORD,
    BASIC_AUTH_USER,
)
from utils.api_client import APIClient


@pytest.fixture
def api_client():
    client = APIClient()
    yield client
    client.session.close()


@pytest.fixture
def auth_client():
    """Client pointed at the auth test service, with no credentials set."""
    client = APIClient(base_url=AUTH_BASE_URL)
    yield client
    client.session.close()


@pytest.fixture
def bearer_client():
    client = APIClient(base_url=AUTH_BASE_URL, token=API_TOKEN)
    yield client
    client.session.close()


@pytest.fixture
def basic_auth_credentials():
    return BASIC_AUTH_USER, BASIC_AUTH_PASSWORD
