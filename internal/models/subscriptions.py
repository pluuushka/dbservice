from sqlalchemy import Column, Integer, DataTime
from .base import Base

class Subscriptions(Base):
    __tablename__ = "subscriptions" # name of table in PostgreSQL

    # fields
    id = Column(Integer)
    user_id = Column(Integer)
    config_id = Column(Integer)
    start_date = Column(DataTime)
    end_date = Column(DataTime)
    cost = Column(Integer)

