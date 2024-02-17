#!/usr/bin/python3
"""
 statment object
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    sess = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    sessio = sess()
    nw_state = State(name='Louisiana')
    sessio.add(nw_state)
    sessio.commit()
    state_add = sessio.query(State).filter(State.name == 'Louisiana').one()
    print(state_add.id)

    sessio.close()
