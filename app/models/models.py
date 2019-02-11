#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import UniqueConstraint
from app import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return ("<User: id={:d}, name='{}', email='{}'>".format(
                self.id, self.name, self.email))

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)

    def __repr__(self):
        return ("<Category: id={:d}, name='{}'"
                " description={}>".format(
                    self.id, self.name, self.description))

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
    category = relationship(Category, backref=backref(
        'items', cascade='all, delete'))
    style = Column(String(250), nullable=False, unique=True)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    def __repr__(self):
        return ("<Item: id={:d}, style='{}'"
                " category_id={:d}, user_id={:d}>".format(
                    self.id, self.style, self.category_id, self.user_id))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'category_id': self.category_id,
            'style': self.style,
            'description': self.description,
            'user_id': self.user_id
        }
