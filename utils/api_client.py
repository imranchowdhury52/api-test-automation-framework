import requests
from config.config import BASE_URL, TIMEOUT


class APIClient:

    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, params=None):
        response = requests.get(
            f"{self.base_url}{endpoint}",
            params=params,
            timeout=TIMEOUT
        )
        return response

    def post(self, endpoint, data=None):
        response = requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            timeout=TIMEOUT
        )
        return response
