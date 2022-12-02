#!/usr/bin/python3
"""
[2;2R[>77;30601;0c]10;rgb:bfbf/bfbf/bfbf]11;rgb:0000/0000/0000Defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Represents a state for a MySQL database.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
