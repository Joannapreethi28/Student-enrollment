from services.enrollment_service import EnrollmentService


class EnrollmentController:

    def __init__(
        self
    ):

        self.enrollment_service = EnrollmentService()

    def enroll_student(
        self,
        student_id,
        teacher_id
    ):

        return self.enrollment_service.enroll_student(
            student_id,
            teacher_id
        )

    def get_all_enrollments(
        self
    ):

        return self.enrollment_service.get_all_enrollments()
