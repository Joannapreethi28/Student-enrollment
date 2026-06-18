from database.db import enrollments


class EnrollmentRepository:

    def add_enrollment(
        self,
        enrollment
    ):

        enrollments.append(
            enrollment
        )

        return enrollment

    def get_all_enrollments(
        self
    ):

        return enrollments


