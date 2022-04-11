from sqlite3 import IntegrityError
from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from . import models, schemas


def get_person(db: Session, person_id: int) -> models.Person:
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def create_person(db: Session, person: schemas.PersonCreate) -> models.Person:
    db_user = models.Person(**person.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_person_by_email(db: Session, email: str) -> models.Person:
    return db.query(models.Person).filter(models.Person.email == email).first()


def get_organization(db: Session, organization_id: int):
    return (
        db.query(models.Organization)
        .filter(models.Organization.id == organization_id)
        .first()
    )


def create_university(db: Session, university: schemas.UniversityCreate):
    db_uni = models.University(**university.dict())
    db.add(db_uni)
    db.commit()
    db.refresh(db_uni)
    return db_uni


def add_student_to_university(db: Session, university_id: int, person_id: int):
    db_uni: models.University = get_university(db, university_id)
    db_person: models.Person = get_person(db, person_id)

    if db_uni is None or db_person is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="University or person not found",
        )

    db_uni.students.append(db_person)
    db.commit()
    db.refresh(db_uni)
    return db_uni


# get university by id
def get_university(db: Session, university_id: int):
    return (
        db.query(models.University)
        .filter(models.University.id == university_id)
        .first()
    )
