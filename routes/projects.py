from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import db
from bson import ObjectId
from schemas.projects import ProjectsBase,ProjectsOut,ProjectsCreate,ProjectsUpdate
router = APIRouter()

@router.post("/", response_model=ProjectsOut)
async def create_project(project: ProjectsCreate):
    # Insert the project into the database
    result = await db.projects.insert_one(project.dict())
    # Get the project back from the database
    new_project = await db.projects.find_one({"_id": result.inserted_id})
    new_project["_id"] = str(new_project["_id"])  # Convert MongoDB ObjectId to string
    return new_project

@router.get("/", response_model=list[ProjectsOut])
async def get_projects():
    projects = await db.projects.find().to_list(100)  # Adjust the limit as needed
    # Convert all MongoDB ObjectIds to string
    for project in projects:
        project["_id"] = str(project["_id"])
    return projects

@router.get("/{project_id}", response_model=ProjectsOut)
async def get_project(project_id: str):
    project = await db.projects.find_one({"_id": ObjectId(project_id)})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project["_id"] = str(project["_id"])
    return project

@router.put("/{project_id}", response_model=ProjectsOut)
async def update_project(project_id: str, project: ProjectsUpdate):
    result = await db.projects.update_one({"_id": ObjectId(project_id)}, {"$set": project.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    updated_project = await db.projects.find_one({"_id": ObjectId(project_id)})
    updated_project["_id"] = str(updated_project["_id"])
    return updated_project

@router.delete("/{project_id}")
async def delete_project(project_id: str):
    result = await db.projects.delete_one({"_id": ObjectId(project_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted"}
