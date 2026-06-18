from services.student_service import StudentService


class StudentController:

    def __init__(self):

        self.student_service = StudentService()

    def add_student(
        self,
        student_id,
        name,
        email,
        phone
    ):

        return self.student_service.add_student(
            student_id,
            name,
            email,
            phone
        )

    def get_all_students(self):

        return self.student_service.get_all_students()

    def get_student_by_id(
        self,
        student_id
    ):

        return self.student_service.get_student_by_id(
            student_id
        )

    def delete_student(
        self,
        student_id
    ):

        return self.student_service.delete_student(
            student_id
        )
