from repositories.student_repository import StudentRepository
from database.session import get_session
from fastapi import Depends
from sqlmodel import Session
from services.student_service import StudentService

def get_student_repository(
    session: Session = Depends(get_session),
) -> StudentRepository:
    return StudentRepository(session)


def get_student_service(
        repository:StudentRepository = Depends(get_student_repository),#"repository is expected to be a StudentRepository object."
)-> StudentService:
    return StudentService(repository)