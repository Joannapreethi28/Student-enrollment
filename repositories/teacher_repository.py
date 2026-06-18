from database.db import teachers


class TeacherRepository:

    def add_teacher(
        self,
        teacher
    ):

        teachers.append(
            teacher
        )

        return teacher

    def get_all_teachers(
        self
    ):

        return teachers

    def get_teacher_by_id(
        self,
        teacher_id
    ):

        for teacher in teachers:

            if teacher.teacher_id == teacher_id:

                return teacher

        return None


