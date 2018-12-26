from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
db = SQLAlchemy(app)

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.UnicodeText(10000), nullable=True)

    @property
    def serialize(self):
        return{
            'id': self.id
            'name': self.name
            'description': self.description
        }

class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.column(db.Integer, ForeignKey('category.id'))
    category = relationship('Category', backref=backref('category', uselist=False))
    style = db.column(db.String(250), nullable=False)
    description = db.column(db.UnicodeText(10000), nullable=False)

    @property
    def serialize(self):
        return{
            'id' = self.id
            'category' = self.category
            'style' = self.style
            'description' = self.description
        }

class User(db.model):
    __tablename__ = 'user'

    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(250), nullable=False)
    email = db.column(db.String(250), nullable=False)

db.create_all()



