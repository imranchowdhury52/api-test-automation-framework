import os

# Every value can be overridden with an environment variable,
# so the same suite runs against different environments without code changes.
BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
AUTH_BASE_URL = os.getenv("AUTH_BASE_URL", "https://httpbin.org")
TIMEOUT = int(os.getenv("API_TIMEOUT", "10"))

API_TOKEN = os.getenv("API_TOKEN", "demo-token")
BASIC_AUTH_USER = os.getenv("BASIC_AUTH_USER", "qa_user")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "qa_password")
