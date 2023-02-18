from datetime import date
from pydantic import validator
from typing import Optional
import re
from email_validator import validate_email, EmailNotValidError


class UserCreate:
    email: str = None
    username: str = None
    password: str = None

    @validator("password", pre=True, always=True)
    def validate_password(cls, value):
        if not value:
            raise ValueError("Password can not be empty")
        if len(value) < 6:
            raise ValueError("Password can not be shorter than 8 characters")
        return value

    @validator("email", pre=True, always=True)
    def validate_email(cls, value):
        if not value:
            raise ValueError("Email can not be empty")
        try:
            validate_email(value)
        except EmailNotValidError:
            raise ValueError("Email is not valid")
        return value

    @validator("username", pre=True, always=True)
    def validate_username(cls, value):
        if not value:
            raise ValueError("Username can not be empty")
        if len(value) < 6:
            raise ValueError("Username can not be shorter than 6 characters")
        if ' ' in value:
            raise ValueError("Username can not include spaces")
        if re.search(r'\bn[i1!][gq][gq3]a\b', value, flags=re.IGNORECASE):
            raise ValueError("Username can not contains blocked words")
        return value


class User:
    email: str = None
    username: str = None
    created_date: Optional[date]
    updated_date: Optional[date]

    class Config:
        orm_mode = True

