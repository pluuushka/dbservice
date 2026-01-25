# models/configs.py
from sqlalchemy import Column, Integer, Boolean
from .base import Base 

class User(Base):
    __tablename__ = 'users'  # name of table in PostgreSQL
    
    # fields
    id = Column(Integer, primary_key=True)
    id_test = Column(Boolean)
    server_id = Column(Integer)
    protocol = Column(String) # need string to be stay formated