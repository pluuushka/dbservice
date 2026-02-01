from sqlalchemy import Column, Integer, BigInteger, DateTime, ForeignKey
from .base import Base

class Subscriptions(Base):
    __tablename__ = "subscriptions" # name of table in PostgreSQL

    # fields
    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    cost = Column(Integer, nullable=True) # only for timurchik can be nullable

