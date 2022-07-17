from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WinningNumber(Base):
    __tablename__ = "Winners"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    bonus = Column(Integer, nullable=False)


class TestTable(Base):
    __tablename__ = "Test"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
