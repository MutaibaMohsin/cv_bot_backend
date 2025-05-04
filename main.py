from fastapi import FastAPI
from routes.education import router as education_router
from routes.expirence import router as experience_router
from routes.auth import router as user_router
from routes.skills import router as skills_router
from routes.achievements import router as achievements_router
from routes.projects import router as projects_router

app = FastAPI()

app.include_router(education_router, prefix="/education", tags=["Education"])
app.include_router(experience_router, prefix="/experience", tags=["Experience"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(skills_router, prefix="/skills", tags=["Skills"])
app.include_router(achievements_router, prefix="/achievements", tags=["Achievements"])
app.include_router(projects_router, prefix="/projects", tags=["Projects"])
