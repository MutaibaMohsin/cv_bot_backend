from fastapi import APIRouter, HTTPException
from schemas.achievements import AchievementsCreate, AchievementsUpdate, AchievementsOut
from database import db
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=AchievementsOut)
async def create_achievement(ach: AchievementsCreate):
    result = await db.achievements.insert_one(ach.dict())
    new_ach = await db.achievements.find_one({"_id": result.inserted_id})
    new_ach["_id"] = str(new_ach["_id"])
    return new_ach

@router.get("/", response_model=list[AchievementsOut])
async def get_all_achievements():
    achievements = await db.achievements.find().to_list(100)
    for ach in achievements:
        ach["_id"] = str(ach["_id"])
    return achievements

@router.get("/{ach_id}", response_model=AchievementsOut)
async def get_achievement(ach_id: str):
    ach = await db.achievements.find_one({"_id": ObjectId(ach_id)})
    if not ach:
        raise HTTPException(status_code=404, detail="Achievement not found")
    ach["_id"] = str(ach["_id"])
    return ach

@router.put("/{ach_id}")
async def update_achievement(ach_id: str, data: AchievementsUpdate):
    result = await db.achievements.update_one({"_id": ObjectId(ach_id)}, {"$set": data.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return {"message": "Achievement updated"}

@router.delete("/{ach_id}")
async def delete_achievement(ach_id: str):
    result = await db.achievements.delete_one({"_id": ObjectId(ach_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return {"message": "Achievement deleted"}
