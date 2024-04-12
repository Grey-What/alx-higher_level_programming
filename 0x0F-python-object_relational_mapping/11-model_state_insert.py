#!/usr/bin/python3
"""
add new object 'Louisiana' to State table in
database 'hbtn_0e_6_usa'
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """add new object to table"""

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
