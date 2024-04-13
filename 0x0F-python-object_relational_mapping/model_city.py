#!/usr/bin/python3
"""
file contain class definition of City
that inherits from declarative base class
"""


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    defines a City that will be part of the system
    Declarative that inherits from Base class
    and link to table called cities

    Args:
    __tablename__ (string): name of table it will be mapped too
    id (int): auto-generated, primary key of table
    name (string): string of 128 char, cannot be NULL
    """
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
