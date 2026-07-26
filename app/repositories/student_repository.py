from sqlmodel import Session, select
from models.student import Student

class StudentRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(self, student: Student) -> Student:
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def get(self, student_id: int) -> Student | None:
        return self.session.get(Student, student_id)

    def list(self) -> list[Student]:
        statement = select(Student)
        return self.session.exec(statement).all()

    def delete(self, student: Student) -> None:
        self.session.delete(student)
        self.session.commit()

    def update(self, student: Student) -> Student:
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student