from fastapi import FastAPI
from routes.courses import router as courses_router

app = FastAPI()

# Inclui as rotas
app.include_router(courses_router)
