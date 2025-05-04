from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

class ProjectsBase(BaseModel):
    name: str  # This is required
    description: str  # This is required
    technologies: Optional[List[str]] = []  # Optional, default is empty list

class ProjectsCreate(ProjectsBase):
    pass

class ProjectsUpdate(ProjectsBase):
    pass

class ProjectsOut(ProjectsBase):
    id: str = Field(default_factory=str, alias="_id")  # MongoDB ObjectId mapped to "id"

    class Config:
        orm_mode = True  # Allows Pydantic to work with non-Pydantic data models like MongoDB
        allow_population_by_field_name = True  # Allows population of the field name "id" as well
