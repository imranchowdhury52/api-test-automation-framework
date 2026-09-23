import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "tests" / "data"


def load_test_data(file_name, key):
    """Load a list of test cases from a JSON file in tests/data."""
    with open(DATA_DIR / file_name, encoding="utf-8") as f:
        return json.load(f)[key]
