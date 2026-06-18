from repositories.teacher_repository import TeacherRepository
from models.teacher import Teacher


class TeacherService:

    def __init__(self):

        self.teacher_repository = TeacherRepository()

    def add_teacher(
        self,
        teacher_id,
        name,
        department
    ):

        teacher = Teacher(
            teacher_id,
            name,
            department
        )

        return self.teacher_repository.add_teacher(
            teacher
        )

    def get_all_teachers(self):

        return self.teacher_repository.get_all_teachers()

    def get_teacher_by_id(
        self,
        teacher_id
    ):

        return self.teacher_repository.get_teacher_by_id(
            teacher_id
        )
