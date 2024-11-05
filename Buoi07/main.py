from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from models import mymodel

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


def find_student_by_id(id):
    students = get_student_from_file()
    for student in students:
        if student["id"] == id:
            return student
    return None

@app.get("/students")
def get_all_students():
    return get_student_from_file()

@app.get("/students/{id}")
def get_all_students(id):
    # students = get_student_from_file()
    # for student in students:
    #     if student["id"] == id:
    #         return student
    # return None
    return find_student_by_id(id)


@app.post("/students")
def insert_new_student(model: mymodel.Student):
    if find_student_by_id(id):
        return {"success": False, "message": f"Exist student {model.id}"}
    students = get_student_from_file()
    students.append({
        "id": model.id, "name": model.name, "gpa": model.gpa
    })
    with open(STUDENT_FILE, "w", encoding="utf8") as f:
        json.dump(students, f, indent=4)
    return {"success": True, "data": model}