from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure
from prettytable import PrettyTable
import textwrap

# Connecting with Local Instance of MongoDB
try:
    client = MongoClient(serverSelectionTimeoutMS=5000)  # 5-second timeout
    db = client['bca']
    faculties_collection = db['faculties']
    courses_collection = db['courses']
    students_collection = db['students']
    client.admin.command('ping')  # Check the connection
    print("Database connection successful!")
except ServerSelectionTimeoutError:
    print("Database connection failed! Please ensure that MongoDB is running.")
    exit()

# Helper function to wrap text
def wrap_text(text, width=30):
    return "\n".join(textwrap.wrap(text, width))

# Methods for CRUD operations
# faculties collection
def list_faculties():
    try:
        table = PrettyTable()
        table.field_names = ["Name", "Post", "Email", "Expertise", "Courses Taught"]
        for faculty in faculties_collection.find():
            table.add_row([
                faculty['name'],
                faculty['post'],
                faculty['email'],
                wrap_text(faculty['expertise']),
                wrap_text(faculty['courses_taught'])
            ])
        print(table)
    except Exception as e:
        print(f"Error listing faculties: {e}")

def add_faculty():
    name = input("Enter the name of the faculty: ").strip()
    post = input("Enter the post: ").strip()
    email = input("Enter the email: ").strip()
    expertise = input("Enter the expertise: ").strip()
    courses_taught = input("Enter the courses taught: ").strip()

    if not all([name, post, email, expertise, courses_taught]):
        print("All fields are required!")
        return

    faculty_detail = {
        "name": name,
        "post": post,
        "email": email,
        "expertise": expertise,
        "courses_taught": courses_taught
    }

    try:
        faculties_collection.insert_one(faculty_detail)
        print("Faculty added successfully!")
    except OperationFailure as e:
        print(f"Error adding faculty: {e}")

def remove_faculty():
    name = input("Enter the name: ").strip()
    if not name:
        print("Name is required!")
        return

    try:
        result = faculties_collection.delete_one({'name': name})
        if result.deleted_count:
            print("Faculty removed successfully!")
        else:
            print("Faculty not found!")
    except OperationFailure as e:
        print(f"Error removing faculty: {e}")

def find_faculty():
    name = input("Enter the name: ").strip()
    if not name:
        print("Name is required!")
        return

    try:
        faculty = faculties_collection.find_one({'name': name})
        if faculty:
            table = PrettyTable()
            table.field_names = ["Name", "Post", "Email", "Expertise", "Courses Taught"]
            table.add_row([
                faculty['name'],
                faculty['post'],
                faculty['email'],
                wrap_text(faculty['expertise']),
                wrap_text(faculty['courses_taught'])
            ])
            print(table)
        else:
            print("Faculty not found!")
    except Exception as e:
        print(f"Error finding faculty: {e}")

# courses collection
def list_courses():
    try:
        table = PrettyTable()
        table.field_names = ["Course Code", "Title", "Year", "Semester", "Pre-Requisites", "Co-Requisites", "Objectives"]
        for course in courses_collection.find():
            table.add_row([
                course['course_code'],
                course['title_of_the_course'],
                course['year'],
                course['semester'],
                wrap_text(course['pre_requisites']),
                wrap_text(course['co_requisites']),
                wrap_text(course['course_objectives'])
            ])
        print(table)
    except Exception as e:
        print(f"Error listing courses: {e}")

def add_course():
    course_code = input("Enter the course code: ").strip()
    title_of_the_course = input("Enter the title of the course: ").strip()
    year = input("Enter the year: ").strip()
    semester = input("Enter the semester: ").strip()
    pre_requisites = input("Enter the pre-requisite: ").strip()
    co_requisites = input("Enter the co-requisite: ").strip()
    course_objectives = input("Enter course objectives: ").strip()

    if not all([course_code, title_of_the_course, year, semester, pre_requisites, co_requisites, course_objectives]):
        print("All fields are required!")
        return

    course_detail = {
        "course_code": course_code,
        "title_of_the_course": title_of_the_course,
        "year": year,
        "semester": semester,
        "pre_requisites": pre_requisites,
        "co_requisites": co_requisites,
        "course_objectives": course_objectives
    }

    try:
        courses_collection.insert_one(course_detail)
        print("Course added successfully!")
    except OperationFailure as e:
        print(f"Error adding course: {e}")

def remove_course():
    course_code = input("Enter the course code: ").strip()
    if not course_code:
        print("Course code is required!")
        return

    try:
        result = courses_collection.delete_one({'course_code': course_code})
        if result.deleted_count:
            print("Course removed successfully!")
        else:
            print("Course not found!")
    except OperationFailure as e:
        print(f"Error removing course: {e}")

def find_course():
    course_code = input("Enter the course code: ").strip()
    if not course_code:
        print("Course code is required!")
        return

    try:
        course = courses_collection.find_one({'course_code': course_code})
        if course:
            table = PrettyTable()
            table.field_names = ["Course Code", "Title", "Year", "Semester", "Pre-Requisites", "Co-Requisites", "Objectives"]
            table.add_row([
                course['course_code'],
                course['title_of_the_course'],
                course['year'],
                course['semester'],
                wrap_text(course['pre_requisites']),
                wrap_text(course['co_requisites']),
                wrap_text(course['course_objectives'])
            ])
            print(table)
        else:
            print("Course not found!")
    except Exception as e:
        print(f"Error finding course: {e}")

# student collection
def list_students():
    try:
        table = PrettyTable()
        table.field_names = ["Enrollment No.", "Name", "Group", "Email", "Address"]
        for student in students_collection.find():
            table.add_row([
                student['enroll_no'],
                student['name'],
                student['group'],
                student['email'],
                wrap_text(student['address'])
            ])
        print(table)
    except Exception as e:
        print(f"Error listing students: {e}")

def add_student():
    name = input("Enter the name of the student: ").strip()
    enroll_no = input("Enter the enrollment no.: ").strip()
    group = input("Enter the group: ").strip()
    email = input("Enter the email: ").strip()
    address = input("Enter the address: ").strip()

    if not all([name, enroll_no, group, email, address]):
        print("All fields are required!")
        return

    student_detail = {
        "name": name,
        "enroll_no": enroll_no,
        "group": group,
        "email": email,
        "address": address
    }

    try:
        students_collection.insert_one(student_detail)
        print("Student added successfully!")
    except OperationFailure as e:
        print(f"Error adding student: {e}")

def remove_student():
    enroll_no = input("Enter the enrollment no.: ").strip()
    if not enroll_no:
        print("Enrollment no. is required!")
        return

    try:
        result = students_collection.delete_one({'enroll_no': enroll_no})
        if result.deleted_count:
            print("Student removed successfully!")
        else:
            print("Student not found!")
    except OperationFailure as e:
        print(f"Error removing student: {e}")

def find_student():
    enroll_no = input("Enter the enrollment no.: ").strip()
    if not enroll_no:
        print("Enrollment no. is required!")
        return

    try:
        student = students_collection.find_one({'enroll_no': enroll_no})
        if student:
            table = PrettyTable()
            table.field_names = ["Enrollment No.", "Name", "Group", "Email", "Address"]
            table.add_row([
                student['enroll_no'],
                student['name'],
                student['group'],
                student['email'],
                wrap_text(student['address'])
            ])
            print(table)
        else:
            print("Student not found!")
    except Exception as e:
        print(f"Error finding student: {e}")

def main_menu():
    while True:
        print("\n1. Faculties\n2. Courses\n3. Students\n4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            faculties_menu()
        elif choice == '2':
            courses_menu()
        elif choice == '3':
            students_menu()
        elif choice == '4':
            print("\nThank You!")
            break
        else:
            print("Invalid Input!")

def faculties_menu():
    while True:
        print("\n1. List all faculties details")
        print("2. Add a new faculty")
        print("3. Remove an existing faculty")
        print("4. Find faculty by name")
        print("5. Previous Menu")
        c = input("Enter your choice: ").strip()
        if c == '1':
            list_faculties()
        elif c == '2':
            add_faculty()
        elif c == '3':
            remove_faculty()
        elif c == '4':
            find_faculty()
        elif c == '5':
            break
        else:
            print("Invalid Input!")

def courses_menu():
    while True:
        print("\n1. List all courses details")
        print("2. Add a new course")
        print("3. Remove an existing course")
        print("4. Find course by code")
        print("5. Previous Menu")
        c = input("Enter your choice: ").strip()
        if c == '1':
            list_courses()
        elif c == '2':
            add_course()
        elif c == '3':
            remove_course()
        elif c == '4':
            find_course()
        elif c == '5':
            break
        else:
            print("Invalid Input!")

def students_menu():
    while True:
        print("\n1. List all students details")
        print("2. Add a new student")
        print("3. Remove an existing student")
        print("4. Find student by enrollment number")
        print("5. Previous Menu")
        c = input("Enter your choice: ").strip()
        if c == '1':
            list_students()
        elif c == '2':
            add_student()
        elif c == '3':
            remove_student()
        elif c == '4':
            find_student()
        elif c == '5':
            break
        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main_menu()
