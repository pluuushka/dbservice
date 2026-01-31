# models/carma.py

from sqlalchemy import Column, Integer, DataTime
from .base import Base

class Carma(Base):
    __tablename__ = "carma" # name of table in PostgreSQL

    # fields
    user_id = Column(Integer, primary_key=True)
    total_points = Column(Integer, nullable=False)
    active_points = Column(Integer, nullable=False)
    last_updated = Column(DataTime, nullable=False) # when it created it is last_updated 

    