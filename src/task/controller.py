from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModel
from fastapi import HTTPException,status

def create_tasks(body:TaskSchema,db:Session):
    data=body.model_dump()
    new_task=TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"]
        )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "status":"Task created successfully..",
        "data":new_task
    }

def get_tasks(db:Session):
    tasks= db.query(TaskModel).all()
    return {
        "status":"all tasks",
        "data": tasks
    }

def get_one_task(task_id: int,db: Session):
    task= db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail="task id is incorrect")
    return{
        "status":"task fetched successfully",
        "data": task
    }

def update_task(body:TaskSchema,task_id:int,db:Session):
    task= db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail="task id is incorrect")
    
    task.title=body.title
    task.description=body.description
    task.is_completed=body.is_completed

    db.add(task)
    db.commit()
    db.refresh(task)

    return {
        "details":"Task updated successfully",
        "data":task
    }