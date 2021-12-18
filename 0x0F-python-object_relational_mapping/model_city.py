#!/usr/bin/python3
"""
contains the class definition of a City
"""

from model_state import Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    "Represents the City class"
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
