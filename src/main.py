from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from auth_handler import signJWT
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


@app.post("/token")
def get_token(user: schemas.PersonCreate, db: Session = Depends(get_db)):
    person: models.Person = crud.get_person_by_email(db, user.email)
    if person is None or person.hashed_password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    return signJWT()
