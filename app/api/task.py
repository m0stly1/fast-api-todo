from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/api"
)

@router.get("/task/{id}")
def get_task(id:int):
    return{"status":"get_task"}

@router.post("/task")
def create_task():
    return{"status":"create_task"}

@router.put("/task")
def update_task():
    return{"status":"update_task"}

@router.delete("/task/{id}")
def delete_task(id:int):
    return{"status":"delete_task"}