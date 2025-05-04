from fastapi import APIRouter, HTTPException
from schemas.skills import SkillsCreate, SkillsUpdate, SkillsOut
from database import db
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=SkillsOut)
async def create_skills(skill: SkillsCreate):
    result = await db.skills.insert_one(skill.dict())
    new_skill = await db.skills.find_one({"_id": result.inserted_id})
    new_skill["_id"] = str(new_skill["_id"])
    return new_skill

@router.get("/", response_model=list[SkillsOut])
async def get_all_skills():
    skills = await db.skills.find().to_list(100)
    for skill in skills:
        skill["_id"] = str(skill["_id"])
    return skills

@router.get("/{skill_id}", response_model=SkillsOut)
async def get_skills(skill_id: str):
    skill = await db.skills.find_one({"_id": ObjectId(skill_id)})
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    skill["_id"] = str(skill["_id"])
    return skill

@router.put("/{skill_id}")
async def update_skills(skill_id: str, data: SkillsUpdate):
    result = await db.skills.update_one({"_id": ObjectId(skill_id)}, {"$set": data.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"message": "Skill updated"}

@router.delete("/{skill_id}")
async def delete_skills(skill_id: str):
    result = await db.skills.delete_one({"_id": ObjectId(skill_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"message": "Skill deleted"}
