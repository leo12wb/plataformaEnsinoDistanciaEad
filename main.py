from fastapi import FastAPI
from routes.courses import router as courses_router
from routes.modules import router as modules_router
from routes.coursesmodules import router as coursesmodules_router
from routes.disciplines import router as disciplines_router

app = FastAPI()

# Inclui as rotas
app.include_router(courses_router)
app.include_router(modules_router)
app.include_router(coursesmodules_router)
app.include_router(disciplines_router)
