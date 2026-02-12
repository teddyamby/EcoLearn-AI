from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, index=True)
    birth_date = Column(Date)
    password_hash = Column(String)

    study_time = Column(Float, default=0.0)
    trees_financed = Column(Integer, default=0)
    co2_consumed = Column(Float, default=0.0)

    courses = relationship("Course", back_populates="user")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    level = Column(String)
    duration = Column(String)
    content = Column(Text)

    co2_generated = Column(Float)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="courses")
