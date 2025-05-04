from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class EducationBase(BaseModel):
    degree: str
    university: str

class EducationCreate(EducationBase):
    pass

class EducationUpdate(EducationBase):
    pass

class EducationOut(EducationBase):
    id: str = Field(default_factory=str, alias="_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
