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
    initial_sidebar_state="collapsed"
)


# ---------------------------------------------------
# CONTROLLERS
# ---------------------------------------------------

student_controller = StudentController()
teacher_controller = TeacherController()
enrollment_controller = EnrollmentController()


# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "active_module" not in st.session_state:
    st.session_state.active_module = "Common Dashboard"

if "student_action" not in st.session_state:
    st.session_state.student_action = "Add Student"

if "teacher_action" not in st.session_state:
    st.session_state.teacher_action = "Add Teacher"

if "enrollment_action" not in st.session_state:
    st.session_state.enrollment_action = "Enroll Student"


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


def page_heading(title, subtitle):
    st.markdown(
        f"""
        <div class="page-heading">
            <h2>{safe(title)}</h2>
            <p>{safe(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_card(title, value, caption):
    st.markdown(
        f"""
        <div class="metric-card">
            <p class="metric-title">{safe(title)}</p>
            <h1>{safe(value)}</h1>
            <p class="metric-caption">{safe(caption)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def action_card(title, description):
    st.markdown(
        f"""
        <div class="action-card">
            <h3>{safe(title)}</h3>
            <p>{safe(description)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def custom_table(headers, rows):
    table_html = '<table class="custom-table">'
    table_html += '<thead><tr>'

    for header in headers:
        table_html += f'<th>{safe(header)}</th>'

    table_html += '</tr></thead>'
    table_html += '<tbody>'

    for row in rows:
        table_html += '<tr>'

        for value in row:
            table_html += f'<td>{safe(value)}</td>'

        table_html += '</tr>'

    table_html += '</tbody></table>'

    st.markdown(
        table_html,
        unsafe_allow_html=True
    )


def set_module(module_name):
    st.session_state.active_module = module_name


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

    section[data-testid="stSidebar"] {
        display: none;
    }

    .hero {
        background: linear-gradient(120deg, #2563eb 0%, #7c3aed 50%, #0891b2 100%);
        padding: 36px;
        border-radius: 28px;
        color: white;
        margin-bottom: 26px;
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

    .nav-box {
        background: rgba(255, 255, 255, 0.88);
        padding: 18px;
        border-radius: 24px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        margin-bottom: 26px;
    }

    .page-heading {
        background: rgba(255, 255, 255, 0.88);
        padding: 22px 26px;
        border-radius: 22px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        margin-bottom: 24px;
    }

    .page-heading h2 {
        color: #0f172a;
        margin-bottom: 5px;
        font-weight: 800;
    }

    .page-heading p {
        color: #475569;
        margin-bottom: 0;
    }

    .metric-card {
        background: rgba(255, 255, 255, 0.94);
        padding: 24px;
        border-radius: 24px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        transition: 0.25s ease;
        min-height: 155px;
        margin-bottom: 18px;
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

    .action-card {
        background: rgba(255, 255, 255, 0.94);
        padding: 24px;
        border-radius: 24px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        min-height: 150px;
        margin-bottom: 12px;
        transition: 0.25s ease;
    }

    .action-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.13);
    }

    .action-card h3 {
        color: #0f172a;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .action-card p {
        color: #475569;
        margin-bottom: 0;
        font-size: 15px;
    }

    .module-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 26px;
        border-radius: 24px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .module-box h3 {
        color: #0f172a;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .module-box p {
        color: #475569;
        margin-bottom: 0;
    }

    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.92);
        padding: 25px;
        border-radius: 24px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
    }

    .custom-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0 12px;
        margin-top: 12px;
    }

    .custom-table thead tr {
        background: linear-gradient(120deg, #2563eb, #7c3aed);
        color: white;
    }

    .custom-table th {
        padding: 16px;
        text-align: left;
        font-size: 15px;
        color: white;
    }

    .custom-table th:first-child {
        border-radius: 16px 0 0 16px;
    }

    .custom-table th:last-child {
        border-radius: 0 16px 16px 0;
    }

    .custom-table tbody tr {
        background: rgba(255, 255, 255, 0.96);
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
        transition: 0.2s ease;
    }

    .custom-table tbody tr:hover {
        transform: scale(1.01);
        box-shadow: 0 14px 32px rgba(15, 23, 42, 0.13);
    }

    .custom-table td {
        padding: 16px;
        color: #334155;
        font-size: 15px;
    }

    .custom-table td:first-child {
        border-radius: 16px 0 0 16px;
        font-weight: 700;
        color: #1d4ed8;
    }

    .custom-table td:last-child {
        border-radius: 0 16px 16px 0;
    }

    .stButton > button {
        border-radius: 14px;
        border: none;
        padding: 0.65rem 1rem;
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
        <p>Module-based web application for managing students, teachers, and enrollments.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# TOP NAVIGATION BAR
# ---------------------------------------------------

st.markdown(
    """
    <div class="nav-box">
    """,
    unsafe_allow_html=True
)

nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    if st.button(
        "Common Dashboard",
        use_container_width=True,
        type="primary" if st.session_state.active_module == "Common Dashboard" else "secondary"
    ):
        set_module("Common Dashboard")

with nav_col2:
    if st.button(
        "Students",
        use_container_width=True,
        type="primary" if st.session_state.active_module == "Students" else "secondary"
    ):
        set_module("Students")

with nav_col3:
    if st.button(
        "Teachers",
        use_container_width=True,
        type="primary" if st.session_state.active_module == "Teachers" else "secondary"
    ):
        set_module("Teachers")

with nav_col4:
    if st.button(
        "Enrollments",
        use_container_width=True,
        type="primary" if st.session_state.active_module == "Enrollments" else "secondary"
    ):
        set_module("Enrollments")

st.markdown(
    """
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# COMMON DASHBOARD
# ---------------------------------------------------

if st.session_state.active_module == "Common Dashboard":

    students = student_controller.get_all_students()
    teachers = teacher_controller.get_all_teachers()
    enrollments = enrollment_controller.get_all_enrollments()

    page_heading(
        "Common Dashboard",
        "Overall summary of the complete Student Enrollment System."
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

    col1, col2, col3 = st.columns(3)

    with col1:
        action_card(
            "Students Module",
            "Manage student registration, student records, and student deletion."
        )

    with col2:
        action_card(
            "Teachers Module",
            "Manage teacher details and view teacher records."
        )

    with col3:
        action_card(
            "Enrollments Module",
            "Enroll students under teachers and view enrollment records."
        )


# ---------------------------------------------------
# STUDENTS DASHBOARD
# ---------------------------------------------------

elif st.session_state.active_module == "Students":

    students = student_controller.get_all_students()
    enrollments = enrollment_controller.get_all_enrollments()

    page_heading(
        "Students Dashboard",
        "Manage all student-related operations from one module."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "Total Students",
            len(students),
            "Registered students"
        )

    with col2:
        metric_card(
            "Student Actions",
            "3",
            "Add, view, and delete"
        )

    with col3:
        metric_card(
            "Linked Enrollments",
            len(enrollments),
            "Enrollment records connected to students"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="module-box">
            <h3>Student Module Actions</h3>
            <p>Select an action card below to work inside the Students module.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        action_card(
            "Add Student",
            "Register a new student with ID, name, email, and phone number."
        )

        if st.button(
            "Open Add Student",
            use_container_width=True,
            key="open_add_student"
        ):
            st.session_state.student_action = "Add Student"

    with col2:
        action_card(
            "View Students",
            "Display all students in a clean table format."
        )

        if st.button(
            "Open View Students",
            use_container_width=True,
            key="open_view_students"
        ):
            st.session_state.student_action = "View Students"

    with col3:
        action_card(
            "Delete Student",
            "Delete a student and automatically remove related enrollments."
        )

        if st.button(
            "Open Delete Student",
            use_container_width=True,
            key="open_delete_student"
        ):
            st.session_state.student_action = "Delete Student"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.session_state.student_action == "Add Student":

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

    elif st.session_state.student_action == "View Students":

        page_heading(
            "View Students",
            "All student records are displayed below."
        )

        students = student_controller.get_all_students()

        if students:

            rows = []

            for student in students:
                data = student.to_dict()

                rows.append(
                    [
                        data.get("student_id"),
                        data.get("name"),
                        data.get("email"),
                        data.get("phone")
                    ]
                )

            custom_table(
                [
                    "Student ID",
                    "Name",
                    "Email",
                    "Phone"
                ],
                rows
            )

        else:

            st.info("No students found")

    elif st.session_state.student_action == "Delete Student":

        page_heading(
            "Delete Student",
            "Select a student and remove the student with related enrollments."
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

                            st.session_state.student_action = "View Students"
                            rerun_app()

                        else:

                            st.error("Student not found")

        else:

            st.info("No students available to delete")


# ---------------------------------------------------
# TEACHERS DASHBOARD
# ---------------------------------------------------

elif st.session_state.active_module == "Teachers":

    teachers = teacher_controller.get_all_teachers()

    page_heading(
        "Teachers Dashboard",
        "Manage all teacher-related operations from one module."
    )

    col1, col2 = st.columns(2)

    with col1:
        metric_card(
            "Total Teachers",
            len(teachers),
            "Teachers currently available"
        )

    with col2:
        metric_card(
            "Teacher Actions",
            "2",
            "Add and view teachers"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="module-box">
            <h3>Teacher Module Actions</h3>
            <p>Select an action card below to work inside the Teachers module.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        action_card(
            "Add Teacher",
            "Register a new teacher with teacher ID, name, and department."
        )

        if st.button(
            "Open Add Teacher",
            use_container_width=True,
            key="open_add_teacher"
        ):
            st.session_state.teacher_action = "Add Teacher"

    with col2:
        action_card(
            "View Teachers",
            "Display all teacher records in a clean table format."
        )

        if st.button(
            "Open View Teachers",
            use_container_width=True,
            key="open_view_teachers"
        ):
            st.session_state.teacher_action = "View Teachers"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.session_state.teacher_action == "Add Teacher":

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

    elif st.session_state.teacher_action == "View Teachers":

        page_heading(
            "View Teachers",
            "All teacher records are displayed below."
        )

        teachers = teacher_controller.get_all_teachers()

        if teachers:

            rows = []

            for teacher in teachers:
                data = teacher.to_dict()

                rows.append(
                    [
                        data.get("teacher_id"),
                        data.get("name"),
                        data.get("department")
                    ]
                )

            custom_table(
                [
                    "Teacher ID",
                    "Name",
                    "Department"
                ],
                rows
            )

        else:

            st.info("No teachers found")


# ---------------------------------------------------
# ENROLLMENTS DASHBOARD
# ---------------------------------------------------

elif st.session_state.active_module == "Enrollments":

    enrollments = enrollment_controller.get_all_enrollments()
    students = student_controller.get_all_students()
    teachers = teacher_controller.get_all_teachers()

    page_heading(
        "Enrollments Dashboard",
        "Manage student-teacher enrollment operations from one module."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "Total Enrollments",
            len(enrollments),
            "Active enrollment records"
        )

    with col2:
        metric_card(
            "Available Students",
            len(students),
            "Students ready for enrollment"
        )

    with col3:
        metric_card(
            "Available Teachers",
            len(teachers),
            "Teachers available for mapping"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="module-box">
            <h3>Enrollment Module Actions</h3>
            <p>Select an action card below to work inside the Enrollments module.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        action_card(
            "Enroll Student",
            "Map a student to a teacher and create an enrollment record."
        )

        if st.button(
            "Open Enroll Student",
            use_container_width=True,
            key="open_enroll_student"
        ):
            st.session_state.enrollment_action = "Enroll Student"

    with col2:
        action_card(
            "View Enrollments",
            "Display all enrollment records in a clean table format."
        )

        if st.button(
            "Open View Enrollments",
            use_container_width=True,
            key="open_view_enrollments"
        ):
            st.session_state.enrollment_action = "View Enrollments"

    st.markdown("<br>", unsafe_allow_html=True)

    if st.session_state.enrollment_action == "Enroll Student":

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

    elif st.session_state.enrollment_action == "View Enrollments":

        page_heading(
            "View Enrollments",
            "All enrollment records are displayed below."
        )

        enrollments = enrollment_controller.get_all_enrollments()

        if enrollments:

            all_keys = []

            for enrollment in enrollments:
                data = enrollment.to_dict()

                for key in data.keys():
                    if key not in all_keys:
                        all_keys.append(key)

            rows = []

            for enrollment in enrollments:
                data = enrollment.to_dict()
                row = []

                for key in all_keys:
                    row.append(data.get(key))

                rows.append(row)

            custom_table(
                all_keys,
                rows
            )

        else:

            st.info("No enrollments found")
