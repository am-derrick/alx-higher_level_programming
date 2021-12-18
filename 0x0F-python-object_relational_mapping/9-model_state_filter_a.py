#!/usr/bin/python3
"""
lists all State objects containing letter a from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sqlalchemy import crreate_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                       argv[2],
                                                                       argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    a = '%a%'
    states = session.query(State).filter(State.name.like(a)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
