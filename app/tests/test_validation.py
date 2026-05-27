import pytest

from app.core.validation import normalize_email, validate_required_text


def test_normalize_email_strips_and_lowercases() -> None:
    assert normalize_email("  UsER@ExaMPLe.com    ") == "user@example.com"


def test_validate_required_text_returns_cleaned_value() -> None:
    result = validate_required_text(
        "  Acme Inc.   ", field_name="organization name", max_length=100
    )

    assert result == "Acme Inc."


def test_validate_required_text_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="organization name is required"):
        validate_required_text("   ", field_name="organization name", max_length=100)


def test_validate_required_text_rejects_too_long_value() -> None:
    with pytest.raises(
        ValueError, match="organization name must be at most 3 characters"
    ):
        validate_required_text(
            "  Acme Inc.   ", field_name="organization name", max_length=3
        )
