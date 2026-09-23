import time

import requests

from config.config import BASE_URL, TIMEOUT
from utils.logger import get_logger

log = get_logger()


class APIClient:
    """Thin wrapper around requests.Session with auth handling and structured logging."""

    def __init__(self, base_url=BASE_URL, token=None, basic_auth=None, timeout=TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
        if token:
            self.set_bearer_token(token)
        if basic_auth:
            self.session.auth = basic_auth

    def set_bearer_token(self, token):
        self.session.headers["Authorization"] = f"Bearer {token}"

    def clear_auth(self):
        self.session.headers.pop("Authorization", None)
        self.session.auth = None

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)

        start = time.perf_counter()
        response = self.session.request(method, url, **kwargs)
        elapsed_ms = round((time.perf_counter() - start) * 1000)

        log.info(
            "method=%s url=%s status=%s elapsed_ms=%s",
            method, url, response.status_code, elapsed_ms,
        )
        if kwargs.get("json") is not None:
            log.debug("request_body=%s", kwargs["json"])
        log.debug("response_body=%s", response.text[:500])
        return response

    def get(self, endpoint, params=None, **kwargs):
        return self.request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint, data=None, **kwargs):
        return self.request("POST", endpoint, json=data, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self.request("PUT", endpoint, json=data, **kwargs)

    def patch(self, endpoint, data=None, **kwargs):
        return self.request("PATCH", endpoint, json=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)
