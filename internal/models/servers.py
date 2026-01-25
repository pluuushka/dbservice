# models/servers.py

from sqlalchemy import Column, Integer, String
from .base import Base

class Servers(Base):
    __tablename__= "servers" # name of table in PostgreSQL

    # fields
    id = Column(Integer, primary_key=True)
    ip = Column(String)
    country = Column(String)
    ssh_key_hash = Column(String)
    monthly_cost = Column(Integer)
    hostname = Column(String)
    max_configs= Column(Integer)
    status = Column(String)
    protocol = Column(String) # need to be string to stay formated for data like "001"
