from fastapi import APIRouter
from schemas.student_schema import StudentCreate, StudentResponse

router = APIRouter(
    prefix="/student",
    tags = ["students"],
)

@router.get("")
def list_students():
    return [
        {
            "id": 1,
            "name": "Prasanna",
            "course": "Python",
        },
        {
            "id": 2,
            "name": "Hari",
            "course": "FastAPI",
        },
    ]

@router.get("/{student_id}")
def get_student(student_id: int):
    return {
        "id": student_id,
        "name": "Unknown Student",
    }

@router.post(
    "/create_student",
    response_model=StudentResponse,
    status_code=201,
    tags=["Students"],
    summary="Create a new student",
    description="Creates a student in the system",
    response_description="Created student",
    deprecated=False,
)
def create_student(student:StudentCreate):
    return {
        "id":1,
        "name":student.name,
        "age":student.age,
        "course":student.course 
    }