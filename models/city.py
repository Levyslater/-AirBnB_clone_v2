#!/usr/bin/python3
""" City Module for HBNB project
    inherits from BaseModel and Base classes
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name
        Adds new attribute '__tablename__' and sets value to 'cities'
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='cities', cascade='all, delete-orphan')