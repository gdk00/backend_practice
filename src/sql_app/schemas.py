from typing import List, Optional

from pydantic import BaseModel


class JwtSchema(BaseModel):
    jwt: str


class PersonBase(BaseModel):
    email: str


class PersonCreate(PersonBase):
    password: str


class Person(PersonBase):
    id: int
    organization_id: Optional[int] = None
    university_id: Optional[int] = None

    class Config:
        orm_mode = True


class OrganizationBase(BaseModel):
    title: str


class OrganizationCreate(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int
    employees: List[Person] = []

    class Config:
        orm_mode = True


class UniversityBase(BaseModel):
    title: str


class UniversityCreate(UniversityBase):
    pass


class University(UniversityBase):
    id: int
    students: List[Person] = []

    class Config:
        orm_mode = True


class UniversityAddStudent(BaseModel):
    person_id: int
    university_id: int
