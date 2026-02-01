from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, BigInteger
from .base import Base

class Carma_Events(Base):
    __tablename__ = "carma_events" # name of table in PostgreSQL

    # fields
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    amount = Column(Integer, nullable=False)
    is_positive = Column(Boolean, nullable=False)
    reason = Column(String(50))
    created_at = Column(DateTime, nullable=False)