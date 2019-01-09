from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
app = Flask(__name__)
 
engine = create_engine('sqlite:///catalog.db')
 
# create a Declarative base class which stores the classes representing tables
Base = declarative_base()
Base.metadata.reflect(bind=engine)
 
# create a configured "Session" class
Session = sessionmaker(bind=engine)
 
# create a Session
session = Session()
 
# create all tables that don't yet exist
def create_tables():
    Base.metadata.create_all(engine)