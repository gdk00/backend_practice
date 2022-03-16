from sqlalchemy.orm import Session

from . import models, schemas


def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def get_organization(db: Session, organization_id: int):
    return (
        db.query(models.Organization)
        .filter(models.Organization.id == organization_id)
        .first()
    )
