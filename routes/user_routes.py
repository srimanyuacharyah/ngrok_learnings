from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import User
from repositories.user_repo import UserRepo
from schemas.user_schemas import UserSchema

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    new_user = User(**user.dict())
    user_repo.add_user(new_user)
    return new_user

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    users = user_repo.get_all_users()
    return users

@router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user = user_repo.get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user    