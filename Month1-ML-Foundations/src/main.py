# Importing pydantic model 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Creating a pydantic model 
class Student(BaseModel):
    name: str
    rollno: int
    marks: int
    branch: str
    result: str

# API endpoint
@app.post("/student_data")
def student_data(student: Student):
    return {
        "message": f"Student name: {student.name}, Roll No: {student.rollno}, Marks: {student.marks}, Branch: {student.branch}, Result Status: {student.result}"
        ,
        "data": student
    } 