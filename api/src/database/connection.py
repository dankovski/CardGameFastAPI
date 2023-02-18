from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config import get_settings
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = f"postgresql://{get_settings().ADMIN_USERNAME}:{get_settings().ADMIN_PASSWORD}@postgres/prod"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
