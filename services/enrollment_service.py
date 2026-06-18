rom repositories.enrollment_repository import EnrollmentRepository
from services.student_service import StudentService
from services.teacher_service import TeacherService
from models.enrollment import Enrollment


class EnrollmentService:

    def __init__(
        self
    ):

        self.enrollment_repository = EnrollmentRepository()

        self.student_service = StudentService()

        self.teacher_service = TeacherService()

    def enroll_student(
        self,
        student_id,
        teacher_id
    ):

        student = self.student_service.get_student_by_id(
            student_id
        )

        teacher = self.teacher_service.get_teacher_by_id(
            teacher_id
        )

        if not student:

            raise Exception(
                "Student not found"
            )

        if not teacher:
          raise Exception(
                "Teacher not found"
            )

        enrollment = Enrollment(
            student_id,
            teacher_id
        )

        return self.enrollment_repository.add_enrollment(
            enrollment
        )

    def get_all_enrollments(
        self
    ):

        return self.enrollment_repository.get_all_enrollments()

