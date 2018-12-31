from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(Category)
    style = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'id' : self.id,
            'category' : self.category,
            'style' : self.style,
            'description' : self.description
        }

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)





