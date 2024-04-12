#!/usr/bin/python3
"""script changes name of State object in database 'hbtn_0e_6_usa'"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """changes name of state with specified id"""

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()
    result = session.query(State).filter(State.id == 2).first()

    if (result is not None):
        result.name = "New Mexico"

    session.commit()
