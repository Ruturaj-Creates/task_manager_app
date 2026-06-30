from fastapi import FastAPI
from src.utils.db import Base,engine
from src.task.router import task_routes

Base.metadata.create_all(engine)

app=FastAPI(title="Task manager App")
app.include_router(task_routes)

