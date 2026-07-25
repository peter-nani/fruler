from fastapi import FastAPI
import uvicorn

from routers.root import router as root_router
from routers.student import router as student_router

app = FastAPI(
    title="Campus Management System",
    version="1.0.0",
)

app.include_router(student_router)
app.include_router(root_router)


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)