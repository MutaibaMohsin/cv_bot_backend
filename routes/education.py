from fastapi import APIRouter, HTTPException
from schemas.education import EducationCreate, EducationUpdate, EducationOut
from database import db
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=EducationOut)
async def create_education(education: EducationCreate):
    result = await db.education.insert_one(education.dict())
    new_education = await db.education.find_one({"_id": result.inserted_id})
    new_education["_id"] = str(new_education["_id"])  # Convert _id to string
    if "cv_id" in new_education and isinstance(new_education["cv_id"], ObjectId):
        new_education["cv_id"] = str(new_education["cv_id"])  # Convert cv_id to string if it's an ObjectId
    return new_education


@router.get("/", response_model=list[EducationOut])
async def get_all_education():
    education_list = await db.education.find().to_list(100)
    for education in education_list:
        education["_id"] = str(education["_id"])  # Convert _id to string
        if "cv_id" in education and isinstance(education["cv_id"], ObjectId):
            education["cv_id"] = str(education["cv_id"])  # Convert cv_id to string if it's an ObjectId
    return education_list


@router.get("/{education_id}", response_model=EducationOut)
async def get_education(education_id: str):
    education = await db.education.find_one({"_id": ObjectId(education_id)})
    if not education:
        raise HTTPException(status_code=404, detail="Education not found")
    education["_id"] = str(education["_id"])
    return education

@router.put("/{education_id}")
async def update_education(education_id: str, data: EducationUpdate):
    result = await db.education.update_one({"_id": ObjectId(education_id)}, {"$set": data.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Education not found")
    return {"message": "Education updated"}

@router.delete("/{education_id}")
async def delete_education(education_id: str):
    result = await db.education.delete_one({"_id": ObjectId(education_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Education not found")
    return {"message": "Education deleted"}
