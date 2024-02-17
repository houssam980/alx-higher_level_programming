#!/usr/bin/python3
"""
prints the first State object from the database
"""
from pip._internal.network import session
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy import create_engine


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    sess = sessionmaker(bind=eng)
    Base.metadata.create_all(eng)
    sessio = sess()

sts = session.query(State).filter(State.name.ilike('%a%'))\
    .order_by(State.id).all()
for state in sts:
    print("{}: {}".format(state.id, state.name))
    sessio.close()
