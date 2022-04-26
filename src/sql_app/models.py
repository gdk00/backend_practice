from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    organization = relationship("Organization", back_populates="employees")
    organization_id = Column(Integer, ForeignKey("organization.id"), nullable=True)
    university = relationship("University", back_populates="students")
    university_id = Column(Integer, ForeignKey("university.id"), nullable=True)

    def __repr__(self) -> str:
        return f"User: {self.email}"


class Organization(Base):
    __tablename__ = "organization"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    employees = relationship("Person", back_populates="organization")


class University(Base):
    __tablename__ = "university"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    students = relationship("Person", back_populates="university")
