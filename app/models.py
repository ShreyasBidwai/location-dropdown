
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    states = relationship("State", back_populates="country")

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship("Country", back_populates="states")
    cities = relationship("City", back_populates="state")

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")
