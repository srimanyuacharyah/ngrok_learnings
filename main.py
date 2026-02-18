from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

students: List["Student"] = []


class Student(BaseModel):
    name: str
    email: str
    age: int
    Roll_number: int
    Department: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/students")
def create_student(student: Student):
    for s in students:
        if s.Roll_number == student.Roll_number:
            raise HTTPException(status_code=400, detail="Student already exists")

    students.append(student)
    return student
@app.get("/students")
def read_students():
    return students

@app.get("/students/{roll}")
def read_student(roll: int):
    for student in students:
        if student.Roll_number == roll:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{roll}")
def update_student(roll: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.Roll_number == roll:
            students[index] = updated_student
            return updated_student

    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{roll}")
def delete_student(roll: int):
    for index, student in enumerate(students):
        if student.Roll_number == roll:
            students.pop(index)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")
