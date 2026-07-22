from fastapi import FastAPI
from students import Student

app = FastAPI()

students = [
    Student(
        id=1,
        name="Ahmad Mustafa",
        age=22,
        course="Computer Science"
    ),
    Student(
        id=2,
        name="Abdul Hadi",
        age=21,
        course="Software Engineering"
    )
]

@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}

@app.post("/students")
def add_student(student: Student):

    students.append(student.dict())

    return {
        "message": "Student added successfully",
        "student": student
    }