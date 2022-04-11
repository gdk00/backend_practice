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
