import sqlite3
from sqlite3 import IntegrityError
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import exc
from sqlalchemy.orm import Session

from auth_handler import decodeJWT, signJWT
from sql_app import crud, database, models, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/person/{person_id}", response_model=schemas.Person)
def get_person(person_id: int, db: Session = Depends(get_db)):
    person = crud.get_person(db, person_id=person_id)
    return person


@app.get("/org/{org_id}", response_model=schemas.Organization)
def get_organization(org_id: int, db: Session = Depends(get_db)):
    org = crud.get_organization(db, organization_id=org_id)
    return org


@app.post("/secret")
def get_secret(jwt_schema: schemas.JwtSchema, db: Session = Depends(get_db)):
    params = decodeJWT(jwt_schema.jwt)
    user = crud.get_person(db, params["user_id"])
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return {"secret": "Super super secret"}


@app.post("/token")
def get_token(user: schemas.PersonCreate, db: Session = Depends(get_db)):
    person: models.Person = crud.get_person_by_email(db, user.email)
    if person is None or person.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    return signJWT(person.id)


@app.post("/person")
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_person(db, person)
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Person with email {person.email} already exists",
        )


# post add students to university
@app.post("/university/student")
def add_student_to_university(
    data: schemas.UniversityAddStudent, db: Session = Depends(get_db)
):
    return crud.add_student_to_university(db, data.university_id, data.person_id)


# add university
@app.post("/university", response_model=schemas.University)
def create_university(
    university: schemas.University,
    db: Session = Depends(get_db),
):
    try:
        return crud.create_university(db, university)
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"University with name {university.title} already exists",
        )


# get university by id
@app.get("/university/{university_id}", response_model=schemas.University)
def get_university(university_id: int, db: Session = Depends(get_db)):
    return crud.get_university(db, university_id)
