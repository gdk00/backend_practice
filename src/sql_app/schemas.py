from typing import List, Optional

from pydantic import BaseModel


class PersonBase(BaseModel):
    email: str


class PersonCreate(PersonBase):
    password: str


class Person(PersonBase):
    id: int
    organization_id: Optional[int] = None

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
