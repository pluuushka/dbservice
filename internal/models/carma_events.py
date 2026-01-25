from sqlalchemy import Column, Integer, Boolean, String, DataTime
from .base import Base

class Carma_Events(Base):
    __tablename__ = "Carma Events" # name of table in PostgreSQL

    # fields
    id = Column(Integer)
    user_id = Column(Integer)
    amount = Column(Integer)
    is_positive = Column(Boolean)
    reason = Column(String)
    created_at = Column(DataTime)