from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions.student_exception import StudentNotFoundException


async def student_not_found_handler(
    request: Request,
    exc: StudentNotFoundException,
):
    return JSONResponse(
        status_code=404,
        content={
            "message": str(exc),
        },
    )


def register_exception_handlers(app: FastAPI) -> None:# That's just one clean way to organize multiple handlers outside main.py.
    app.add_exception_handler(
        StudentNotFoundException,
        student_not_found_handler,
    )