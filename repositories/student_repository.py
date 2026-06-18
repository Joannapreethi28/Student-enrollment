from database.db import students, enrollments


class StudentRepository:

    def add_student(self, student):

        students.append(student)

        return student

    def get_all_students(self):

        return students

    def get_student_by_id(self, student_id):

        for student in students:

            if student.student_id == student_id:

                return student

        return None

    def delete_student(self, student_id):

        student_to_delete = None

        for student in students:

            if student.student_id == student_id:

                student_to_delete = student

                break

        if student_to_delete is None:
          return False

        students.remove(student_to_delete)

        enrollments[:] = [
            enrollment
            for enrollment in enrollments
            if enrollment.student_id != student_id
        ]

        return True

