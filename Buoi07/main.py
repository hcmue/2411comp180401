from fastapi import FastAPI
import json

app = FastAPI()

# Chạy UD: fastapi dev main.py

@app.get("/")
def root():
    return {"message": "Welcome to Python FastAPI"}

STUDENT_FILE = "studentdata.json"
def get_student_from_file():
    try:
        with open(STUDENT_FILE, "r", encoding="utf8") as myfile:
            result = json.load(myfile)
            return result
    except:
        return []

@app.get("/students")
def get_all_students():
    return get_student_from_file()

@app.get("/students/{id}")
def get_all_students(id):
    students = get_student_from_file()
    for student in students:
        if student["id"] == id:
            return student
    return None