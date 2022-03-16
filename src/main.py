from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import database, models, crud, schemas

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
