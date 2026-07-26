from repositories.student_repository import StudentRepository
from database.session import get_session
from fastapi import Depends
from sqlmodel import Session

def get_student_repository(
    session: Session = Depends(get_session),
) -> StudentRepository:
    return StudentRepository(session)