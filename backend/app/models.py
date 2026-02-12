from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic = Column(String)
    level = Column(String)
    duration = Column(String)
    content = Column(Text)
    time_spent = Column(Integer, default=0)  # minutes
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="courses")
