from typing import Union
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    student_id: str | None = Field(default=None, index=True)
    gpa: float | None = Field(default = 0)

    __tablename__ = "student"


engine = create_engine("mysql+pymysql://root:@localhost/fastapik48")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/students/")
def create_student(sv: Student, session: SessionDep) -> Student:
    session.add(sv)
    session.commit()
    session.refresh(sv)
    return sv


@app.get("/students/")
def read_students(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Student]:
    students = session.exec(select(Student).offset(offset).limit(limit)).all()
    return students


@app.get("/students/{student_id}")
def read_student(student_id: int, session: SessionDep) -> Student:
    std = session.get(Student, student_id)
    if not std:
        raise HTTPException(
            status_code=404,
            detail=f"Student {student_id} not found"
        )
    return std


@app.delete("/students/{student_id}")
def delete_student(student_id: int, session: SessionDep):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Hero {student_id} not found")
    session.delete(student)
    session.commit()
    return {"success": True}