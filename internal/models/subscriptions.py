from sqlalchemy import Column, Integer, DataTime
from .base import Base

class Subscriptions(Base):
    __tablename__ = "subscriptions" # name of table in PostgreSQL

    # fields
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    config_id = Column(Integer, primary_key=True)
    start_date = Column(DataTime, nullable=False)
    end_date = Column(DataTime, nullable=False)
    cost = Column(Integer, nullable=True) # only for timurchik can be nullable

