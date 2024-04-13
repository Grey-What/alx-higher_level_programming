#!/usr/bin/python3
"""
script prints all City object in database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """print all cities objects in database"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(City, State).join(State).all()

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
