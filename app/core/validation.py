def normalize_email(email: str) -> str:
    return email.strip().lower()


def validate_required_text(value: str, *, field_name: str, max_length: int) -> str:
    cleaned = value.strip()

    if not cleaned:
        raise ValueError(f"{field_name} is required")

    if len(cleaned) > max_length:
        raise ValueError(f"{field_name} must be at most {max_length} characters")

    return cleaned
