#!/usr/bin/python3
# prints the State object with the name.
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':
    usr_name, usr_pass, db_name, state = argv[1], argv[2], argv[3], argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (usr_name, usr_pass, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    f = False
    for state in session.query(State):
        if state.name == state:
            print("{}".format(state.id))
            f = True
            break
    if not f:
        print("Not found")
