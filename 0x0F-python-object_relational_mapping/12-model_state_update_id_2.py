#!/usr/bin/python3
"""
changes the name of a State object
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
    rename_state = sessio.query(State).filter(State.id == 2).first()
    rename_state.name = 'New Mexico'
    sessio.commit()
    """clossing session"""
    sessio.close()
