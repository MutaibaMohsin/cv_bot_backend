from pydantic import BaseModel, Field
from typing import Optional,List
from bson import ObjectId

class ExperienceBase(BaseModel):
    position: str
    company: str
    location: str
    description: Optional[List[str]] = None

class ExperienceCreate(ExperienceBase):
    pass

class ExperienceUpdate(ExperienceBase):
    pass

class ExperienceOut(ExperienceBase):
    id: str = Field(default_factory=str, alias="_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
