# api/users/controllers.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.auth import models
from api.auth.controllers import get_current_user
from api.auth.schemas import UserOut
from api.utils import crud
from api.utils.dependencies import get_db

router = APIRouter()


@router.get("/{user_id}", response_model=UserOut)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    # Fetch the user to be retrieved
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Authorization Logic
    if current_user.id != user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=403, detail="Not authorized to access this user"
        )

    return user


@router.get("/me/", response_model=UserOut)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user


# Add more user-related endpoints as needed
