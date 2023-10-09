## @package db
#
# Responsible for manage the database.

from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float, Date, Boolean, ARRAY, TypeDecorator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from db.handlers import engine

import json

Base = declarative_base()
metadata = Base.metadata


class ArrayType(TypeDecorator):
    """ Sqlite-like does not support arrays.
        Let's use a custom type decorator.

        See http://docs.sqlalchemy.org/en/latest/core/types.html#sqlalchemy.types.TypeDecorator
    """
    impl = String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)

    def copy(self):
        return ArrayType(self.impl.length)


class Athlete(Base):
    __tablename__ = 'athlete'

    id_athlete = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(Integer)
    sex = Column(String)
    birthdate = Column(String)
    age = Column(Integer)
    height = Column(Integer)
    weight = Column(Float)
    sport = Column(String)

    def __init__(self, name, cpf, sex, birthdate, age, height, weight, sport):
        self.name = name
        self.cpf = cpf
        self.sex = sex
        self.birthdate = birthdate
        self.age = age
        self.height = height
        self.weight = weight
        self.sport = sport


class Training(Base):
    __tablename__ = 'training'

    id_training = Column(Integer, primary_key=True)
    name = Column(String)
    number_of_hits = Column(Integer)
    sequence = Column(ArrayType())
    is_random = Column(Boolean)

    def __init__(self, name, number_of_hits, sequence, is_random):
        self.name = name
        self.number_of_hits = number_of_hits
        self.sequence = sequence
        self.is_random = is_random


Base.metadata.create_all(engine)
