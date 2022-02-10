from pydantic import BaseModel
from typing import Optional
from enum import Enum

from app.core.database import Base

class Status(str, Enum):
    doing='doing'
    not_done='not done'

class TaskCreate(BaseModel):
    title: str
    status: Status

class TaskUpdate(BaseModel):
    id: int
    status: Status

class Config:
    orm_mode = True
