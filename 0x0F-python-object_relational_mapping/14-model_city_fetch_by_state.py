import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City



if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    sess = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    sessio = sess()
    cities = sessio.query(State, City) \
                    .filter(State.id == City.state_id)
    for cit in cities:
        print("{}: ({}) {}".format(cit.State.name, cit.City.id, cit.City.name))

    sessio.close()
