import streamlit as st
import html

from controllers.student_controller import StudentController
from controllers.teacher_controller import TeacherController
from controllers.enrollment_controller import EnrollmentController


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Student Enrollment System",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------
# CONTROLLERS
# ---------------------------------------------------

student_controller = StudentController()
teacher_controller = TeacherController()
enrollment_controller = EnrollmentController()


# ---------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------

def rerun_app():
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()


def clean(value):
    return value.strip() if isinstance(value, str) else value


def safe(value):
    if value is None:
        return ""
    return html.escape(str(value))


def to_dict_list(items):
    return [item.to_dict() for item in items]


def page_heading(title, subtitle):
    st.markdown(
        f"""
        <div class="page-heading">
            <h2>{title}</h2>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_card(title, value, caption):
    st.markdown(
        f"""
        <div class="metric-card">
            <p class="metric-title">{title}</p>
            <h1>{value}</h1>
            <p class="metric-caption">{caption}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(135deg, #eef2ff 0%, #f8fafc 45%, #e0f7fa 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #1e293b 60%, #0f172a 100%);
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    .hero {
        background: linear-gradient(120deg, #2563eb 0%, #7c3aed 50%, #0891b2 100%);
        padding: 35px;
        border-radius: 26px;
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 20px 45px rgba(37, 99, 235, 0.25);
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 8px;
        font-weight: 800;
        color: white;
    }

    .hero p {
        font-size: 17px;
        opacity: 0.95;
        margin-bottom: 0;
        color: white;
    }

    .page-heading {
        background: rgba(255, 255, 255, 0.82);
        padding: 22px 26px;
        border-radius: 20px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        margin-bottom: 22px;
    }

    .page-heading h2 {
        color: #0f172a;
        margin-bottom: 4px;
        font-weight: 800;
    }

    .page-heading p {
        color: #475569;
        margin-bottom: 0;
    }

    .metric-card {
        background: rgba(255, 255, 255, 0.92);
        padding: 24px;
        border-radius: 22px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        transition: 0.25s ease;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.13);
    }

    .metric-title {
        color: #64748b;
        font-size: 15px;
        margin-bottom: 8px;
        font-weight: 600;
    }

    .metric-card h1 {
        color: #1d4ed8;
        font-size: 42px;
        margin: 0;
        font-weight: 800;
    }

    .metric-caption {
        color: #475569;
        margin-top: 8px;
        margin-bottom: 0;
        font-size: 14px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 24px;
        border-radius: 22px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        margin-bottom: 20px;
    }

    .glass-card h3 {
        color: #0f172a;
        margin-bottom: 8px;
    }

    .glass-card p {
        color: #475569;
        margin-bottom: 0;
    }

    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 22px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
    }

    .student-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0 12px;
        margin-top: 10px;
    }

    .student-table thead tr {
        background: linear-gradient(120deg, #2563eb, #7c3aed);
        color: white;
    }

    .student-table th {
        padding: 16px;
        text-align: left;
        font-size: 15px;
    }

    .student-table th:first-child {
        border-radius: 16px 0 0 16px;
    }

    .student-table th:last-child {
        border-radius: 0 16px 16px 0;
    }

    .student-table tbody tr {
        background: rgba(255, 255, 255, 0.94);
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
        transition: 0.2s ease;
    }

    .student-table tbody tr:hover {
        transform: scale(1.01);
        box-shadow: 0 14px 32px rgba(15, 23, 42, 0.13);
    }

    .student-table td {
        padding: 16px;
        color: #334155;
        font-size: 15px;
    }

    .student-table td:first-child {
        border-radius: 16px 0 0 16px;
        font-weight: 700;
        color: #1d4ed8;
    }

    .student-table td:last-child {
        border-radius: 0 16px 16px 0;
    }

    .simple-card {
        background: rgba(255, 255, 255, 0.92);
        padding: 18px 22px;
        border-radius: 18px;
        border-left: 6px solid #2563eb;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.08);
        margin-bottom: 14px;
    }

    .teacher-card {
        border-left-color: #7c3aed;
    }

    .enrollment-card {
        border-left-color: #0891b2;
    }

    .card-title {
        color: #0f172a;
        font-size: 18px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .card-text {
        color: #475569;
        font-size: 14px;
        margin-bottom: 2px;
    }

    .delete-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 24px;
        border-radius: 22px;
        border: 1px solid rgba(239, 68, 68, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        margin-top: 24px;
    }

    .delete-box h3 {
        color: #991b1b;
        margin-bottom: 8px;
    }

    .delete-box p {
        color: #64748b;
    }

    .stButton > button {
        border-radius: 14px;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: 700;
        background: linear-gradient(120deg, #2563eb, #7c3aed);
        color: white;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 24px rgba(37, 99, 235, 0.3);
        color: white;
    }

    .stTextInput input {
        border-radius: 12px;
    }

    h1, h2, h3 {
        color: #0f172a;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>Student Enrollment System</h1>
        <p>Manage students, teachers, and enrollments with a modern interactive dashboard.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# SIDEBAR MENU
# ---------------------------------------------------

st.sidebar.markdown("## Navigation")

menu = st.sidebar.radio(
    "Choose a page",
    [
        "Dashboard",
        "Add Student",
        "View Students",
        "Delete Student",
        "Add Teacher",
        "View Teachers",
        "Enroll Student",
        "View Enrollments"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Project")
st.sidebar.markdown("Student Enrollment System")
st.sidebar.markdown("Built using Streamlit and Python")


# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

if menu == "Dashboard":

    students = student_controller.get_all_students()
    teachers = teacher_controller.get_all_teachers()
    enrollments = enrollment_controller.get_all_enrollments()

    page_heading(
        "Dashboard",
        "Overview of students, teachers, and enrollment records."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "Total Students",
            len(students),
            "Students currently available"
        )

    with col2:
        metric_card(
            "Total Teachers",
            len(teachers),
            "Teachers currently available"
        )

    with col3:
        metric_card(
            "Total Enrollments",
            len(enrollments),
            "Active enrollment records"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns(2)

    with left:
        st.markdown(
            """
            <div class="glass-card">
                <h3>Student Module</h3>
                <p>Add, view, and delete students. When a student is deleted, related enrollments are also removed.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:
        st.markdown(
            """
            <div class="glass-card">
                <h3>Enrollment Module</h3>
                <p>Enroll students under teachers and view all enrollment records in one place.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------
# ADD STUDENT
# ---------------------------------------------------

elif menu == "Add Student":

    page_heading(
        "Add Student",
        "Enter student details and save them into the system."
    )

    with st.form("add_student_form", clear_on_submit=True):

        col1, col2 = st.columns(2)

        with col1:
            student_id = st.text_input("Student ID")
            email = st.text_input("Email")

        with col2:
            name = st.text_input("Name")
            phone = st.text_input("Phone")

        submitted = st.form_submit_button(
            "Save Student",
            use_container_width=True
        )

        if submitted:

            student_id = clean(student_id)
            name = clean(name)
            email = clean(email)
            phone = clean(phone)

            if not student_id or not name or not email or not phone:

                st.warning("Please fill all student details")

            elif student_controller.get_student_by_id(student_id):

                st.error("Student ID already exists")

            else:

                student_controller.add_student(
                    student_id,
                    name,
                    email,
                    phone
                )

                st.success("Student added successfully")


# ---------------------------------------------------
# VIEW STUDENTS
# ---------------------------------------------------

elif menu == "View Students":

    page_heading(
        "View Students",
        "View all students in a clean table format."
    )

    students = student_controller.get_all_students()

    if students:

        table_rows = ""

        for student in students:

            data = student.to_dict()

            table_rows += f"""
            <tr>
                <td>{safe(data.get("student_id"))}</td>
                <td>{safe(data.get("name"))}</td>
                <td>{safe(data.get("email"))}</td>
                <td>{safe(data.get("phone"))}</td>
            </tr>
            """

        st.markdown(
            f"""
            <table class="student-table">
                <thead>
                    <tr>
                        <th>Student ID</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="delete-box">
                <h3>Delete Student</h3>
                <p>Select a student below if you want to remove the student and related enrollments.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        student_options = {}

        for student in students:
            data = student.to_dict()
            label = f"{data.get('student_id')} - {data.get('name')}"
            student_options[label] = data.get("student_id")

        selected_student = st.selectbox(
            "Select Student to Delete",
            list(student_options.keys())
        )

        confirm_delete = st.checkbox(
            "I confirm that I want to delete this student"
        )

        if st.button(
            "Delete Selected Student",
            use_container_width=True
        ):

            if not confirm_delete:

                st.warning("Please confirm before deleting")

            else:

                student_id = student_options[selected_student]

                result = student_controller.delete_student(
                    student_id
                )

                if result:

                    st.success(
                        "Student and related enrollments deleted successfully"
                    )

                    rerun_app()

                else:

                    st.error("Student not found")

    else:

        st.info("No students found")


# ---------------------------------------------------
# DELETE STUDENT
# ---------------------------------------------------

elif menu == "Delete Student":

    page_heading(
        "Delete Student",
        "Choose a student and remove the student with related enrollments."
    )

    students = student_controller.get_all_students()

    if students:

        student_options = {}

        for student in students:
            data = student.to_dict()
            label = f"{data.get('student_id')} - {data.get('name')}"
            student_options[label] = data.get("student_id")

        with st.form("delete_student_form"):

            selected_student = st.selectbox(
                "Select Student",
                list(student_options.keys())
            )

            confirm = st.checkbox(
                "I confirm that I want to delete this student"
            )

            submitted = st.form_submit_button(
                "Delete Student",
                use_container_width=True
            )

            if submitted:

                if not confirm:

                    st.warning("Please confirm before deleting")

                else:

                    student_id = student_options[selected_student]

                    result = student_controller.delete_student(
                        student_id
                    )

                    if result:

                        st.success(
                            "Student and related enrollments deleted successfully"
                        )

                        rerun_app()

                    else:

                        st.error("Student not found")

    else:

        st.info("No students available to delete")


# ---------------------------------------------------
# ADD TEACHER
# ---------------------------------------------------

elif menu == "Add Teacher":

    page_heading(
        "Add Teacher",
        "Enter teacher details and save them into the system."
    )

    with st.form("add_teacher_form", clear_on_submit=True):

        col1, col2 = st.columns(2)

        with col1:
            teacher_id = st.text_input("Teacher ID")

        with col2:
            name = st.text_input("Teacher Name")

        department = st.text_input("Department")

        submitted = st.form_submit_button(
            "Save Teacher",
            use_container_width=True
        )

        if submitted:

            teacher_id = clean(teacher_id)
            name = clean(name)
            department = clean(department)

            if not teacher_id or not name or not department:

                st.warning("Please fill all teacher details")

            else:

                teacher_controller.add_teacher(
                    teacher_id,
                    name,
                    department
                )

                st.success("Teacher added successfully")


# ---------------------------------------------------
# VIEW TEACHERS
# ---------------------------------------------------

elif menu == "View Teachers":

    page_heading(
        "View Teachers",
        "View all teacher records in the system."
    )

    teachers = teacher_controller.get_all_teachers()

    if teachers:

        for teacher in teachers:

            data = teacher.to_dict()

            st.markdown(
                f"""
                <div class="simple-card teacher-card">
                    <div class="card-title">{safe(data.get("name"))}</div>
                    <div class="card-text"><b>ID:</b> {safe(data.get("teacher_id"))}</div>
                    <div class="card-text"><b>Department:</b> {safe(data.get("department"))}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info("No teachers found")


# ---------------------------------------------------
# ENROLL STUDENT
# ---------------------------------------------------

elif menu == "Enroll Student":

    page_heading(
        "Enroll Student",
        "Select a student and teacher to create an enrollment record."
    )

    students = student_controller.get_all_students()
    teachers = teacher_controller.get_all_teachers()

    with st.form("enroll_student_form"):

        if students:

            student_options = {}

            for student in students:
                data = student.to_dict()
                label = f"{data.get('student_id')} - {data.get('name')}"
                student_options[label] = data.get("student_id")

            selected_student = st.selectbox(
                "Select Student",
                list(student_options.keys())
            )

            student_id = student_options[selected_student]

        else:

            st.warning("No students available. Add a student first.")
            student_id = ""

        if teachers:

            teacher_options = {}

            for teacher in teachers:
                data = teacher.to_dict()
                label = f"{data.get('teacher_id')} - {data.get('name')}"
                teacher_options[label] = data.get("teacher_id")

            selected_teacher = st.selectbox(
                "Select Teacher",
                list(teacher_options.keys())
            )

            teacher_id = teacher_options[selected_teacher]

        else:

            st.warning("No teachers available. Add a teacher first.")
            teacher_id = ""

        submitted = st.form_submit_button(
            "Enroll Student",
            use_container_width=True
        )

        if submitted:

            if not student_id or not teacher_id:

                st.warning("Student and teacher are required for enrollment")

            else:

                try:

                    enrollment_controller.enroll_student(
                        student_id,
                        teacher_id
                    )

                    st.success("Enrollment successful")

                except Exception as e:

                    st.error(str(e))


# ---------------------------------------------------
# VIEW ENROLLMENTS
# ---------------------------------------------------

elif menu == "View Enrollments":

    page_heading(
        "View Enrollments",
        "View all student-teacher enrollment records."
    )

    enrollments = enrollment_controller.get_all_enrollments()

    if enrollments:

        for enrollment in enrollments:

            data = enrollment.to_dict()

            card_details = ""

            for key, value in data.items():
                card_details += f"""
                <div class="card-text">
                    <b>{safe(key)}:</b> {safe(value)}
                </div>
                """

            st.markdown(
                f"""
                <div class="simple-card enrollment-card">
                    <div class="card-title">Enrollment Record</div>
                    {card_details}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info("No enrollments found")
