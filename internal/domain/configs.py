# models/configs.py
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, BigInteger
from .base import Base 

class Configs(Base):
    __tablename__ = 'configs'  # name of table in PostgreSQL
    
    # fields
    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.user_id'))
    subscription_id = Column(Integer, ForeignKey('subscriptions.id')) #  user can be identify by subscription_id
    is_test = Column(Boolean, nullable=False)
    server_id = Column(Integer, ForeignKey('servers.id'), nullable=False)
    protocol = Column(String(20)) # need string to be stay formated