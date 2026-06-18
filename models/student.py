class Student:

    def __init__(
        self,
        student_id,
        name,
        email,
        phone
    ):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }


