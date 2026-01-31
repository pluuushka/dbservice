from sqlalchemy import Column, Integer, Boolean, String, DataTime
from .base import Base

class Carma_Events(Base):
    __tablename__ = "Carma Events" # name of table in PostgreSQL

    # fields
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    is_positive = Column(Boolean, nullable=False)
    reason = Column(String(50))
    created_at = Column(DataTime, nullable=False)