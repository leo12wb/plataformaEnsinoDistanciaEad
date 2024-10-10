from pydantic import BaseModel

from typing import Optional

class Disciplines(BaseModel):
    id: Optional[int] = None  # Campo id opcional
    title: str
    description: str = None