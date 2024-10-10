from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from models.courses import Courses
from repositories.courses import (
    create as repoCreate,
    readAll as repoReadAll,
    readOne as repoReadOne,
    update as repoUpdate,
    delete as repoDelete,
)

router = APIRouter()

@router.post("/courses", response_model=Courses)
def create(courses: Courses):
    return repoCreate(courses)

@router.get("/courses", response_model=List[Courses])
def readAll():
    return repoReadAll()

@router.get("/courses/{id}", response_model=Courses)
def read(id: int):
    courses = repoReadOne(id)
    if courses is None:
        raise HTTPException(status_code=404, detail="not found")
    return courses

@router.put("/courses/{id}", response_model=Courses)
def update(id: int, courses: Courses):
    return repoUpdate(id, courses)

@router.delete("/courses/{id}")
def delete(id: int):
    repoDelete(id)
    return {"id": id}

# @router.delete("/courses/{id}", response_model=Dict[str, Any])
# def delete(id: int):
#     repoDelete(id)
#     return {"id": id}