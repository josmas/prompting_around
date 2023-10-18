from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    __abstract__ = True

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(100))

    interactions = relationship("Interaction", back_populates="user")

class Interaction(Base):
    __tablename__ = 'interactions'
    id = Column(Integer, primary_key=True)
    action = Column(String(50))
    model_name = Column(String(50))
    input_tokens = Column(Integer)
    output_tokens = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="interactions")
