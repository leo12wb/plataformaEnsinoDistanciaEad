from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from models.disciplines import Disciplines
from repositories.disciplines import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/disciplines", response_model=Disciplines)
def create(disciplines: Disciplines):
    return repoCreate(disciplines)

@router.get("/disciplines", response_model=List[Disciplines])
def readAll():
    return repoReadAll()

@router.get("/disciplines/{id}", response_model=Disciplines)
def read(id: int):
    disciplines = repoReadOne(id)
    if disciplines is None:
        raise HTTPException(status_code=404, detail="not found")
    return disciplines

@router.put("/disciplines/{id}", response_model=Disciplines)
def update(id: int, disciplines: Disciplines):
    return repoUpdate(id, disciplines)

@router.delete("/disciplines/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}
