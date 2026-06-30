from fastapi import FastAPI
from src.utils.db import Base,engine
from src.task.models import TaskModel

Base.metadata.create_all(engine)

app=FastAPI(title="Task manager App")


