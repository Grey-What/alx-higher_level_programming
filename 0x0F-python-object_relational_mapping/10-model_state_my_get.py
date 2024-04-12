#!/usr/bin/python3
"""
print State object in database 'hbtn_0e_6_usa'
where name attribute match argument received
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """retrieve object whos name match argument received"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(State).filter(State.name == argv[4]).first()

    if (result is not None):
        print(result.id)
    else:
        print("Not found")
