#!/usr/bin/python3
"""file contains class definition that is mapped to MySQL tables
   using the Declarative System, defined in terms of a base class
   instance
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """represents a State and links to MySQL table

       Atr:
           __tablename__ (str): represent table name of class
           id (int, Primary key): represents id of state
           name (str): represent name of state
    """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
