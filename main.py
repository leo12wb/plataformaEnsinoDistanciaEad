from fastapi import FastAPI
from routes.courses import router as courses_router
from routes.modules import router as modules_router

app = FastAPI()

# Inclui as rotas
app.include_router(courses_router)
app.include_router(modules_router)
