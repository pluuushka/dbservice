from sqlalchemy import Column, Integer, String, DataTime
from .base import Base

class Applications(Base):
    __tablename__ = "applications" # name of table in PostgreSQL

    # fields
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    subscription_id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    currency = Column(String(10), nullable=False)
    type = Column(String(10), nullable=False)
    status = Column(String(10), nullable=False)
    created_at = Column(DataTime, nullable=False)

    

