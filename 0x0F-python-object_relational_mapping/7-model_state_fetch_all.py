#!/usr/bin/python3
# lists all State objects from the database hbtn_0e_6_usa
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':
    usr_name, usr_pass, db_name = argv[1], argv[2], argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (usr_name, usr_pass, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
