from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class AchievementsBase(BaseModel):
    name: str
    organization:str
    description: str

class AchievementsCreate(AchievementsBase):
    pass

class AchievementsUpdate(AchievementsBase):
    pass

class AchievementsOut(AchievementsBase):
    id: str = Field(default_factory=str, alias="_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
