class Teacher:

    def __init__(
        self,
        teacher_id,
        name,
        department
    ):
        self.teacher_id = teacher_id
        self.name = name
        self.department = department

    def to_dict(self):

        return {
            "teacher_id": self.teacher_id,
            "name": self.name,
            "department": self.department
        }

