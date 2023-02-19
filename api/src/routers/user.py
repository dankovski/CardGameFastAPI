from fastapi import APIRouter, status, Depends, HTTPException
from ..schemas.user import UserCreate, User
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..utils.user import UserUtils

user_router = APIRouter()


@user_router.post("/", response_model=User, response_model_exclude_none=True)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user_by_email = UserUtils.get_user_by_email(db, email=user.email)
    db_user_by_username = UserUtils.get_user_by_username(db, username=user.username)
    if db_user_by_email or db_user_by_username:
        raise HTTPException(status_code=400,
                            detail=list(filter(None, ["Email already registered" if db_user_by_email else None,
                                                 "Username already registered" if db_user_by_username else None])))
    return UserUtils.create_user(db=db, user=user)
