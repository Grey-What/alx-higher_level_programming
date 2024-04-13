#!/usr/bin/python3
"""
delete all State objects that contain the letter a from database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """list State object that meet condition of containing an a"""

    engine = create_engine("mysql+mysqldb://{}:{}@localhost: \
                            3306/{}".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()
    result = session.query(State).filter(State.name.contains('a')).all()

    if result is not None:
        for row in result:
            session.delete(row)

    session.commit()
    session.close()
