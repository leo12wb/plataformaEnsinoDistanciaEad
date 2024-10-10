from pydantic import BaseModel

from datetime import date
from typing import Optional

class Courses(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    title: str
    description: str = None
    start_date: date = None
    end_date: date = None
    status: str