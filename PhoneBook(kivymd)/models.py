from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

engine = create_engine("sqlite:///phones.sqlite", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phones = relationship("Phone", cascade="all,delete", back_populates='user')

    def __str__(self):
        return self.name


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    phones = relationship("Phone", cascade="all,delete", back_populates='user')
    user = relationship("User", back_populates="phones")

    def __str__(self):
        return self.phone

Base.metadata.create_all(engine)