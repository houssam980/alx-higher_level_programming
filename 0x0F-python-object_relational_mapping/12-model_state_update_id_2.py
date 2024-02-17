#!/usr/bin/python3
"""
 
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    sess = sessionmaker(bind=eng)
    Base.metadata.create_all(eng)
    sessio = sess()
    rename = sessio.query(State).filter(State.id == 2).first()
    rename.name = 'New Mexico'
    sessio.commit()

    sessio.close()
