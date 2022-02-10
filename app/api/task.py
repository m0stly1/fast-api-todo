from fastapi import APIRouter, HTTPException
from app.task import service
from app.schemas import *

router = APIRouter(
    prefix="/api"
)

@router.get("/task")
def get_tasks():
    tasks = service.get_all()
    if tasks is None:
       raise HTTPException(status_code=404, detail="Not Found")
    return tasks


@router.get("/task/{id}")
def get_task(id:int):
    task = service.get_task(id)
    if task is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return task


@router.post("/task", status_code=201)
def create_task(task: TaskCreate):
    service.create_task(task)
    return{"response":"create_task"}


@router.put("/task", status_code=204)
def update_task(task: TaskUpdate):
    task = service.update_task(task)
    if task is None:
       raise HTTPException(status_code=404)
    return task

# will only return 204
@router.delete("/task/{id}", status_code=204)
def delete_task(id:int):
    return service.delete_task(id)