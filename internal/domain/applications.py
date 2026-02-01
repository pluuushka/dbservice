from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger
from .base import Base

class Applications(Base):
    __tablename__ = "applications" # name of table in PostgreSQL

    # fields
    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    amount = Column(Integer, nullable=False)
    currency = Column(String(10), nullable=False)
    type = Column(String(10), nullable=False)
    status = Column(String(10), nullable=False)
    created_at = Column(DateTime, nullable=False)

    

