from fastapi import APIRouter, HTTPException, status

from app.schemas.users import UserCreate, UserRead
from app.services.users import create_user, get_user_by_id

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(payload: UserCreate) -> UserRead:
    try:
        user = create_user(payload)
    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(ex)
        ) from ex
    return user


@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
def get_user_endpoint(user_id: str) -> UserRead:
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {user_id} not found",
        )

    return user
