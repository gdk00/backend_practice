from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    organization = relationship("Organization", back_populates="employees")
    organization_id = Column(Integer, ForeignKey("organization.id"), nullable=True)

    def __repr__(self) -> str:
        return f"User: {self.email}"


class Organization(Base):
    __tablename__ = "organization"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    employees = relationship("Person", back_populates="organization")
