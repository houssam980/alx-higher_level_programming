#!/usr/bin/python3
"""
list all states
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":


    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)


    sess = sessionmaker(bind=eng)
    sessio = sess()
    Base.metadata.create_all(eng)

    stte = sessio.query(State).order_by(State.id).all()
    for state in stte:
        print("{}: {}".format(state.id, state.name))
    sessio.close()
