rom repositories.student_repository import StudentRepository
from models.student import Student


class StudentService:

    def __init__(self):

        self.student_repository = StudentRepository()

    def add_student(
        self,
        student_id,
        name,
        email,
        phone
    ):

        student = Student(
            student_id,
            name,
            email,
            phone
        )

        return self.student_repository.add_student(
            student
        )

    def get_all_students(self):

        return self.student_repository.get_all_students()

    def get_student_by_id(
        self,
        student_id
    ):

        return self.student_repository.get_student_by_id(
            student_id
        )

    def delete_student(
        self,
        student_id
    ):

        return self.student_repository.delete_student(
            student_id
        )


