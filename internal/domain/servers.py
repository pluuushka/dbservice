# models/servers.py

from sqlalchemy import Column, Integer, String
from .base import Base

class Servers(Base):
    __tablename__= "servers" # name of table in PostgreSQL

    # fields
    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    ip = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    ssh_key_hash = Column(String(50), nullable=False)
    monthly_cost = Column(Integer, nullable=False)
    hostname = Column(String(20), nullable=False, unique=True) # hostname must be unique
    max_configs= Column(Integer, nullable=False)
    status = Column(String(10), nullable=False)
    protocol = Column(String(20), nullable=False) # need to be string to stay formated for data like "001"
