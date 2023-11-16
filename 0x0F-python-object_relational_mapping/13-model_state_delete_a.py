#!/usr/bin/python3

"""
del * State objects with a name having the letter 'a' from the hbtn_0e_6_usa DB

"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)
    session.commit()
