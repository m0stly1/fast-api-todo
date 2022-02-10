from ..schemas import *
from ..models import *
from ..core.database import session


def get_all():
    tasks = session.query(Task).all()
    if tasks is None: 
        return
    
    return tasks


def create_task(request: TaskCreate):
    task = Task(title = request.title, status = request.status)
    session.add(task)
    session.commit()
    session.refresh(task)


def get_task(id: int):
    task = session.query(Task).get(id)
    if task is None: 
        return
    
    return task


def update_task(request: TaskUpdate):
    task = session.query(Task).get(request.id)
    if task is None:
        return

    task.status = request.status
    
    session.commit()
    session.refresh(task)
    return task

def delete_task(id:int):
    task = get_task(id)
    if task is None:
        return
    
    session.delete(task)
    session.commit()
    return