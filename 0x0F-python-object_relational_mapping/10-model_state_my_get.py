#!/usr/bin/python3
"""
  list all states passed as args
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
    stts = sessio.query(State).filter(State.name == sys.argv[4]).one_or_none()

    if stts is None:
        print("Not found")
    else:
        print(stts.id)
        """closing session"""

    sessio.close()
    
