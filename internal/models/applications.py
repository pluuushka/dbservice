from sqlalchemy import Column, Integer, String, DataTime
from .base import Base

class Applications(Base):
    __tablename__ = "applications" # name of table in PostgreSQL

    # fields
    id = Column(Integer)
    user_id = Column(Integer)
    subscription_id = Column(Integer)
    amount = Column(Integer)
    currency = Column(String)
    type = Column(String)
    status = Column(String)
    created_at = Column(DataTime)

    

