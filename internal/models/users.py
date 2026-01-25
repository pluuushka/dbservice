# models/users.py
from sqlalchemy import Column, BigInteger, Boolean, String
from .base import Base  # all tables inherit from it

class User(Base):
    __tablename__ = 'users'  # name of table in PostgreSQL
    
    # fields
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String)
    invited_by = Column(BigInteger)
    can_take_test = Column(Boolean)
    rank = Column(String)