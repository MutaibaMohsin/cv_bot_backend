from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if MONGO_URI is None:
    raise ValueError("MongoDB URI not found in environment variables")

client = AsyncIOMotorClient(MONGO_URI)
db = client["cv_database"]

def get_collection(collection_name: str):
    return db[collection_name]

user_collection = get_collection("users")
education_collection = get_collection("education")
experience_collection = get_collection("experience")
projects_collection = get_collection("projects")
skills_collection = get_collection("skills")
achievements_collection = get_collection("achievements")
experience_collection = get_collection("experience")