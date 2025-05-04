from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class SkillsBase(BaseModel):
    category: str
    items: List[str] 

class SkillsCreate(SkillsBase):
    pass

class SkillsUpdate(SkillsBase):
    pass

class SkillsOut(SkillsBase):
    id: str = Field(default_factory=str, alias="_id")
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
