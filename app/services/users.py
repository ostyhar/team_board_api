from uuid import uuid4

from app.core.validation import normalize_email, validate_required_text
from app.schemas.users import UserCreate, UserRead

_USERS_BY_ID: dict[str, UserRead] = {}
_USERS_EMAILS: set[str] = set()


def create_user(payload: UserCreate) -> UserRead:
    user_id = str(uuid4())
    user_email = normalize_email(payload.email)

    if user_email in _USERS_EMAILS:
        raise ValueError(f"{user_email} already exists")

    user_display_name = validate_required_text(
        payload.display_name, field_name="display_name", max_length=100
    )
    user = UserRead(id=user_id, email=user_email, display_name=user_display_name)

    _USERS_BY_ID[user.id] = user
    _USERS_EMAILS.add(user_email)

    return user


def get_user_by_id(user_id: str) -> UserRead | None:
    return _USERS_BY_ID.get(user_id, None)
