from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import UniqueConstraint
from app import Base


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class Item(Base):
    __tablename__ = 'item'
    __table_args__ = {'extend_existing': True}
    
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category, backref=backref('items', cascade='all, delete'))
    style = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'id' : self.id,
            'category' : self.category,
            'style' : self.style,
            'description' : self.description
        }

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
