#!/usr/bin/python3

"""
city module
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String


Base = declarative_base()


class City(Base):
    """base class for all cities"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
