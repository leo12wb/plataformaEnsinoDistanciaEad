from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from models.modules import Modules
from repositories.modules import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/modules", response_model=Modules)
def create(courses: Modules):
    return repoCreate(courses)

@router.get("/modules", response_model=List[Modules])
def readAll():
    return repoReadAll()

@router.get("/modules/{id}", response_model=Modules)
def read(id: int):
    courses = repoReadOne(id)
    if courses is None:
        raise HTTPException(status_code=404, detail="not found")
    return courses

@router.put("/modules/{id}", response_model=Modules)
def update(id: int, courses: Modules):
    return repoUpdate(id, courses)

@router.delete("/modules/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

# @router.delete("/courses/{id}", response_model=Dict[str, Any])
# def delete(id: int):
#     repoDelete(id)
#     return {"id": id}