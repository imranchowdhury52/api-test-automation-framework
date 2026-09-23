# REST API Test Automation Framework

![CI](https://github.com/imranchowdhury52/api-test-automation-framework/actions/workflows/ci.yml/badge.svg)

A modular REST API test automation framework built with Python, Pytest and Requests.
It covers request and response validation, authentication handling, data-driven tests,
JSON schema validation, structured logging, and CI execution with GitHub Actions.

---

## Tech Stack

- Python 3.10+
- Pytest
- Requests
- jsonschema
- pytest-html
- GitHub Actions

---

## Features

| Feature | Where |
|---|---|
| Reusable API client on `requests.Session` (GET, POST, PUT, PATCH, DELETE) | `utils/api_client.py` |
| Authentication handling: Bearer token and HTTP Basic auth | `utils/api_client.py`, `tests/test_auth.py` |
| Data-driven tests with test data kept in JSON | `tests/data/users.json`, `utils/data_loader.py` |
| Response schema validation with JSON Schema | `schemas/`, `utils/schema_validator.py` |
| Structured `key=value` logging of every request (method, URL, status, response time) | `utils/api_client.py`, `pytest.ini` |
| Config from environment variables, with defaults | `config/config.py` |
| Markers for suite selection: `smoke`, `regression`, `negative`, `auth`, `schema` | `pytest.ini` |
| HTML and JUnit reports, uploaded as CI artifacts | `.github/workflows/ci.yml` |

---

## Project Structure

```text
api-test-automation-framework/
├── .github/workflows/ci.yml   # CI pipeline
├── config/config.py           # environment-driven configuration
├── schemas/                   # JSON Schemas for response validation
├── tests/
│   ├── data/users.json        # test data for data-driven tests
│   ├── test_users.py          # CRUD, filtering, negative cases
│   ├── test_auth.py           # bearer + basic auth, positive and negative
│   └── test_schema_validator.py
├── utils/
│   ├── api_client.py          # session-based client with auth + logging
│   ├── data_loader.py
│   ├── logger.py
│   └── schema_validator.py
├── conftest.py                # shared fixtures
└── pytest.ini                 # markers, logging, test paths
```

---

## Test Coverage

**Users API** ([JSONPlaceholder](https://jsonplaceholder.typicode.com))
- List users, validated against a JSON Schema, with a unique-ID check
- Get user by ID (data-driven), validated against the full user schema
- Filter by username (data-driven)
- Create (data-driven, including non-ASCII names), update (PUT), partial update (PATCH), delete
- Negative: invalid IDs (zero, just out of range, very large, non-numeric), unknown endpoint, filter with no match

**Authentication** ([httpbin](https://httpbin.org))
- Valid bearer token accepted; missing token rejected with 401; token cleared mid-session
- Basic auth with valid credentials; wrong password rejected with 401

**Schema validator self-tests**
- Makes sure invalid payloads are actually rejected, so a broken schema can't let everything pass

---

## Run Tests Locally

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

pytest -v                      # all tests
pytest -m smoke                # smoke suite only
pytest -m "negative or auth"   # combine markers
pytest --html=reports/report.html --self-contained-html
```

Logs are written to the console and to `reports/test_run.log`:

```text
2026-09-23T16:24:21 level=INFO logger=api method=GET url=https://httpbin.org/bearer status=200 elapsed_ms=540
```

### Configuration

| Variable | Default |
|---|---|
| `API_BASE_URL` | `https://jsonplaceholder.typicode.com` |
| `AUTH_BASE_URL` | `https://httpbin.org` |
| `API_TIMEOUT` | `10` |
| `API_TOKEN` | `demo-token` |
| `BASIC_AUTH_USER` / `BASIC_AUTH_PASSWORD` | `qa_user` / `qa_password` |

---

## Author

Imran Chowdhury · [GitHub](https://github.com/imranchowdhury52) · [LinkedIn](https://www.linkedin.com/in/imran-chowdhury-187599102)
