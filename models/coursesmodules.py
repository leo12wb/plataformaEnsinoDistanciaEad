from pydantic import BaseModel

from typing import Optional

class Coursesmodules(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    course_Id: int
    module_Id: int
    ordenation: int
