#!/usr/bin/python3

from sys import argv
from model_state import Base, state, new_name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    nueva_persona = state(name=argv[4])
    session.add(nueva_persona)
    session.commit()

    states = session.query(state).order_by(state.id).all()
    for state1 in states:
        print('{}: {}'.format(state1.id, state1.name))
    session.close()
