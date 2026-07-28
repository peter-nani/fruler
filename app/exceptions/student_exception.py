
class StudentNotFoundException(Exception):
    def __init__(self, student_id: int):
        self.student_id = student_id
        super().__init__(f"Student with id {student_id} does not exist.")