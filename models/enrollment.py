class Enrollment:

    def __init__(
        self,
        student_id,
        teacher_id
    ):
        self.student_id = student_id
        self.teacher_id = teacher_id

    def to_dict(self):

        return {
            "student_id": self.student_id,
            "teacher_id": self.teacher_id
        }
