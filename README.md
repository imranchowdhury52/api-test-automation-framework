# REST API Test Automation Framework

A simple and modular REST API automation framework built using Python and Pytest.

This project demonstrates API testing best practices including reusable client design,
positive and negative test coverage, and CI integration.

---

## Tech Stack

- Python 3.x
- Pytest
- Requests
- GitHub Actions (CI)

---

##  Features

- Reusable API client abstraction
- Configuration-driven base URL and timeout
- Positive test scenarios (GET, POST)
- Negative test validation (404 case)
- CI pipeline using GitHub Actions
- Clean and modular folder structure

---

## Test Coverage Overview

### Positive Scenarios
- Retrieve list of users
- Create a new user

### Negative Scenario
- Validate 404 response for non-existing user


## Run Tests Locally

1. Clone the Repository
2. Create a virtual environment
    python -m venv venv
    venv\Scripts\activate
3. Install dependencies
    pip install -r requirements.txt
4. Run tests
    pytest -v

