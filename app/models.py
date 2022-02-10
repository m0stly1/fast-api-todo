from .core.database import Base
from sqlalchemy import Column, Integer, String

class Task(Base):
    __tablename__ = "todo"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    status=Column(String)