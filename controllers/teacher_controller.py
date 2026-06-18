from services.teacher_service import TeacherService


class TeacherController:

    def __init__(
        self
    ):

        self.teacher_service = TeacherService()

    def add_teacher(
        self,
        teacher_id,
        name,
        department
    ):

        return self.teacher_service.add_teacher(
            teacher_id,
            name,
            department
        )

    def get_all_teachers(
        self
    ):

        return self.teacher_service.get_all_teachers()

    def get_teacher_by_id(
        self,
        teacher_id
    ):

        return self.teacher_service.get_teacher_by_id(
            teacher_id
        )

