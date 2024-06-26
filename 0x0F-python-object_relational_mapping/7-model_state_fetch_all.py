#!/usr/bin/python3
"""
List all the state Objects from the database hbtn_0e_6_usa,
By connecting to database using create_engine from sqlalchemy
and Creating a session to interact with database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    establish connection and create session
    to retrieve all state objects
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    for inst in session.query(State).order_by(State.id):
        print("{}: {}".format(inst.id, inst.name))
