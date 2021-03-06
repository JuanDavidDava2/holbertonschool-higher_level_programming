#!/usr/bin/python3
# deletes all State objects with a name containing the letter a
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':
    usr_name, usr_pass, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            usr_name,
            usr_pass,
            db_name),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session\
            .query(City, State)\
            .filter(City.state_id == State.id)\
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
