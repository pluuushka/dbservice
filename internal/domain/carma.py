# models/carma.py

from sqlalchemy import Column, Integer, DateTime, ForeignKey, BigInteger
from .base import Base

class Carma(Base):
    __tablename__ = "carma" # name of table in PostgreSQL

    # fields
    user_id = Column(BigInteger, ForeignKey('users.user_id'), primary_key=True)
    total_points = Column(Integer, default=0, nullable=False)
    active_points = Column(Integer, default=0, nullable=False)
    last_updated = Column(DateTime, nullable=False) # when it created it is last_updated 

    