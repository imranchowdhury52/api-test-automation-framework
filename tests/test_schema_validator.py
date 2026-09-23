import pytest
from jsonschema import ValidationError

from utils.schema_validator import assert_matches_schema

VALID_CREATED_USER = {"id": 11, "name": "Mahir", "job": "QA"}


@pytest.mark.schema
def test_validator_accepts_valid_payload():
    assert_matches_schema(VALID_CREATED_USER, "created_user.json")


@pytest.mark.schema
@pytest.mark.negative
@pytest.mark.parametrize(
    "payload",
    [
        {"name": "Mahir", "job": "QA"},
        {"id": "11", "name": "Mahir", "job": "QA"},
        {"id": 11, "name": None, "job": "QA"},
    ],
    ids=["missing id", "id as string", "null name"],
)
def test_validator_rejects_invalid_payload(payload):
    """Guards against a schema that silently accepts anything."""
    with pytest.raises(ValidationError):
        assert_matches_schema(payload, "created_user.json")
