# models/users.py
from sqlalchemy import Column, BigInteger, Boolean, String
from .base import Base  # all tables inherit from it

class User(Base):
    __tablename__ = 'users'  # name of table in PostgreSQL
    
    # fields
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    invited_by = Column(BigInteger)
    can_take_test = Column(Boolean, nullable=False)
    rank = Column(String(10), nullable=False)