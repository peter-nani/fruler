from fastapi import APIRouter, Depends
from schemas.student_schema import StudentCreate, StudentResponse
from database.session import get_session
from sqlmodel import Session, select
from models.student import Student

router = APIRouter(
    prefix="/student",
    tags = ["students"],
)

@router.get("/students_all")
def get_all_students(session: Session = Depends(get_session)):
    statement = select(Student)
    students = session.exec(statement).all()
    return students

@router.post("/create_student_object")
def student_object(
    student_create:StudentCreate,
    session:Session = Depends(get_session)
    ):
    student = Student.model_validate(student_create)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

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


