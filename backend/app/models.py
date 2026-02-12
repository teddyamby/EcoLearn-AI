from sqlalchemy import Column, Integer, String, Date, Float
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, index=True)
    birth_date = Column(Date)
    password_hash = Column(String)

    # 📊 Données écologiques
    study_time = Column(Float, default=0.0)  # en heures
    co2_consumed = Column(Float, default=0.0)  # en grammes
    trees_financed = Column(Integer, default=0)
