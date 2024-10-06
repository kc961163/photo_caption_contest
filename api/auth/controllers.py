# api/auth/controllers.py

from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from api.auth import models, schemas
from api.utils import crud, utils
from api.utils.dependencies import get_db

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login/"
)  # Correct if router prefix is /api/auth


@router.post("/register/", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user with the same email already exists
    existing_user = crud.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Check if username is taken
    existing_username = crud.get_user_by_username(db, username=user.username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    # Create a new user using CRUD operation
    new_user = crud.create_user(db=db, user=user)
    return new_user


@router.post("/login/", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    # Authenticate the user
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Verify the password
    if not utils.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create JWT token
    access_token_expires = timedelta(minutes=utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


# Dependency to get the current user based on JWT
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> models.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, utils.SECRET_KEY, algorithms=[utils.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@router.get("/protected/", response_model=dict)
def protected_route(current_user: models.User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! This is a protected route."}
