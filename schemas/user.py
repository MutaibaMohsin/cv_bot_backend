from pydantic import BaseModel, Field,EmailStr,validator
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator("password")
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return v

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
