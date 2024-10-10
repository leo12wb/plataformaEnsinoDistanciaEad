from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from models.coursesmodules import Coursesmodules
from repositories.coursesmodules import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/coursesmodules", response_model=Coursesmodules)
def create(coursesmodules: Coursesmodules):
    return repoCreate(coursesmodules)

@router.get("/coursesmodules", response_model=List[Coursesmodules])
def readAll():
    return repoReadAll()

@router.get("/coursesmodules/{id}", response_model=Coursesmodules)
def read(id: int):
    coursesmodules = repoReadOne(id)
    if coursesmodules is None:
        raise HTTPException(status_code=404, detail="not found")
    return coursesmodules

@router.put("/coursesmodules/{id}", response_model=Coursesmodules)
def update(id: int, coursesmodules: Coursesmodules):
    return repoUpdate(id, coursesmodules)

@router.delete("/coursesmodules/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}
