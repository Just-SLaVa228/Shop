from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    commodity = relationship("Commodity", back_populates="author")

class Commodity(Base):
    __tablename__ = "commodity"

    id = Column(Integer, primary_key=True)
    title= Column(String) 
    price= Column(Integer)

    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship("Author", back_populates="commodity")
