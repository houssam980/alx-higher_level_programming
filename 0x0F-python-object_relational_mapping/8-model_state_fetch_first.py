#!/usr/bin/python3
"""
prints the first State object from the database
"""


from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy import create_engine

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    sess = sessionmaker(bind=engine)
    sessio = sess()

    result = sessio.query(State).first()
    print("{}: {}".format(result.id, result.name))
