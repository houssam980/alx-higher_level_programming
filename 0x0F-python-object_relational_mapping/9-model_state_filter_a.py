#!/usr/bin/python3
"""
  list all states with letter a 
"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Sess = sessionmaker(bind=eng)
    Base.metadata.create_all(eng)
    sessio = Sess()
    states = sessio.query(State).filter(State.name.ilike('%a%')) \
                    .order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        """closing session"""
    sessio.close()
