from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# STUDENT DATA MODEL
class Student(BaseModel):
    name: str
    age: int
    course: str


# STUDENTS LIST
students = [
    {
        "id": 1,
        "name": "Gouri",
        "age": 22,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Rohit",
        "age": 23, 
        "course": "FastAPI"
    }
]


# HOME API
@app.get("/")
def home():
    return {
        "message": "Student Management System API is running"
    }


# GET ALL STUDENTS API
@app.get("/students")
def get_students():
    return {
        "students": students
    }


# GET STUDENT BY ID API
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return {
                "student": student
            }

    return {
        "message": "Student not found"
    }


# CREATE STUDENT API
@app.post("/students")
def create_student(student: Student):

   

    students.append(new_student)

    return {
        "message": "Student created successfully",
        "student": new_student
    }


# UPDATE STUDENT API
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    for existing_student in students:

        if existing_student["id"] == student_id:

            existing_student["name"] = student.name
            existing_student["age"] = student.age
            existing_student["course"] = student.course

            return {
                "message": "Student updated successfully",
                "student": existing_student
            }

    return {
        "message": "Student not found"
    }


# DELETE STUDENT API
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

  
            return {
                "message": "Student deleted successfully",
                "student": student
            }

    return {
        "message": "Student not found"
    }