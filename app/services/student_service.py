from models.student import Student
from repositories.student_repository import StudentRepository
from exceptions.student_exception import StudentNotFoundException

class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def get_student(self, student_id:int)->Student:
        student = self.repository.get(student_id)

        if student is None:
            raise StudentNotFoundException(student_id)

        return Student