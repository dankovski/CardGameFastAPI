from ..models.user import UserModel
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate
import hashlib
from ..config import get_settings


class UserUtils:

    @classmethod
    def create_user(cls, db: Session, user: UserCreate):
        m = hashlib.sha256()
        m.update((user.password + get_settings().SECRET_KEY).encode())
        hashed_password = m.digest()
        db_user = UserModel(email=user.email, hashed_password=hashed_password, username=user.username)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @classmethod
    def get_user_by_id(cls, db: Session, user_id: int):
        return db.query(UserModel).filter(UserModel.id == user_id).first()

    @classmethod
    def get_user_by_email(cls, db: Session, email: str):
        return db.query(UserModel).filter(UserModel.email == email).first()

    @classmethod
    def get_user_by_username(cls, db: Session, username: str):
        return db.query(UserModel).filter(UserModel.username == username).first()
