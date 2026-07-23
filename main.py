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
        age=20,
        course="Software Engineering"
    ),
        Student(
        id=3,
        name="Faizan Mudassir",
        age=21,
        course="Software Engineering"
    ),
        Student(
        id=4,
        name="Ahmed Furqan",
        age=21,
        course="Computer Science"
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
        if student.id == student_id:
            return student

    return {"message": "Student not found"}

@app.post("/students")
def add_student(student: Student):

    students.append(student)

    return { "message": "Student added successfully"}

@app.put("/students")
def update_student(id: int, name: str, age: int, course: str):
    for student in students:
        if student.id == id:
            student.name = name
            student.age = age
            student.course = course

            return {"message": "Student updated successfully"}

    return {"message": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            
            return {"message": "Student deleted successfully"}

    return {"message": "Student not found"}