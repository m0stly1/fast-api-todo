from pydantic import BaseModel
from typing import Optional

from app.core.database import Base


class TaskCreate(BaseModel):
    title: str
    status: str

class TaskUpdate(BaseModel):
    id: int
    title: Optional[str]
    status: Optional[str]


class Config:
    orm_mode = True