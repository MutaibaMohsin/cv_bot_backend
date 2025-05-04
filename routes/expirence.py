from fastapi import APIRouter, HTTPException
from schemas.expirence import ExperienceCreate, ExperienceUpdate, ExperienceOut
from database import db
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=ExperienceOut)
async def create_experience(exp: ExperienceCreate):
    result = await db.experience.insert_one(exp.dict())
    new_exp = await db.experience.find_one({"_id": result.inserted_id})
    new_exp["_id"] = str(new_exp["_id"])
    return new_exp

@router.get("/", response_model=list[ExperienceOut])
async def get_all_experience():
    experience = await db.experience.find().to_list(100)
    for exp in experience:
        exp["_id"] = str(exp["_id"])
    return experience

@router.get("/{exp_id}", response_model=ExperienceOut)
async def get_experience(exp_id: str):
    exp = await db.experience.find_one({"_id": ObjectId(exp_id)})
    if not exp:
        raise HTTPException(status_code=404, detail="Experience not found")
    exp["_id"] = str(exp["_id"])
    return exp

@router.put("/{exp_id}")
async def update_experience(exp_id: str, data: ExperienceUpdate):
    result = await db.experience.update_one({"_id": ObjectId(exp_id)}, {"$set": data.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Experience not found")
    return {"message": "Experience updated"}

@router.delete("/{exp_id}")
async def delete_experience(exp_id: str):
    result = await db.experience.delete_one({"_id": ObjectId(exp_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Experience not found")
    return {"message": "Experience deleted"}
