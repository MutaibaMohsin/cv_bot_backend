from pydantic import BaseModel, Field,EmailStr,validator
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
