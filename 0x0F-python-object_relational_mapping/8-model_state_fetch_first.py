#!/usr/bin/python3
"""Script that prints first State object from database 'hbtn_0e_6_usa'"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """retrieves first State Object"""

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if (first_state is None):
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
