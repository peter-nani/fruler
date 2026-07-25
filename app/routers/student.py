from fastapi import APIRouter

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