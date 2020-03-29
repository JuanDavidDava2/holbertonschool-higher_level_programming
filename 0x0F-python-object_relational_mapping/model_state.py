#!/usr/bin/python3
# It defines a State model
# Inherits from SQLAlchemy Base and links to the MySQL table states.

""" Model State """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class State.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
