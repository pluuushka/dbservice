# models/configs.py
from sqlalchemy import Column, Integer, Boolean, String
from .base import Base 

class User(Base):
    __tablename__ = 'users'  # name of table in PostgreSQL
    
    # fields
    id = Column(Integer, primary_key=True)
    subscription_id = Column(Integer, primary_key=True) #  user can be identify by subscription_id
    is_test = Column(Boolean, nullable=False)
    server_id = Column(Integer, unique=True, nullable=False)
    protocol = Column(String(20)) # need string to be stay formated