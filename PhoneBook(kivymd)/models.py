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

    @classmethod
    def add(cls, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter(cls.name.ilike(f'%{name}%'))

    @classmethod
    def find_by_phone(cls, phone):
        return session.query(cls).join(Phone).filter(Phone.phone.ilike(f'%{phone}%'))

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def delete_by_id(cls, user_id):
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="phones")

    def __str__(self):
        return self.phone

    @classmethod
    def add(cls, phone, user):
        phone = cls(phone=phone, user=user)
        session.add(phone)
        session.commit()
        return phone

Base.metadata.create_all(engine)
