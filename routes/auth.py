from fastapi import APIRouter, HTTPException, Depends
from schemas.user import UserCreate, UserLogin, UserOut
from database import db
from utils.auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/signup", response_model=UserOut)
async def signup(user: UserCreate):
    existing = await db.users.find_one({"username": user.username})
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_pw = hash_password(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_pw
    del user_dict["password"]
    await db.users.insert_one(user_dict)
    return {"username": user.username, "email": user.email}

@router.post("/login")
async def login(user: UserLogin):
    db_user = await db.users.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user["username"]})
    return {"access_token": token, "token_type": "bearer"}
