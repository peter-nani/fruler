from fastapi import FastAPI
import uvicorn
from routers.root import router as root_router
from routers.student import router as student_router
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from database.engine import engine
import models
from exceptions.handlers import register_exception_handlers

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Campus Management System",
    version="1.0.0",
    lifespan=lifespan,
)

register_exception_handlers(app)

app.include_router(student_router)
app.include_router(root_router)


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)