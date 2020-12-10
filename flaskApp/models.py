# Create database schema here 
from flaskApp import db

class User(db.Model):
    __tablename__ = 'user' # Already created table 
    id = db.Column('id', db.Integer, primary_key=True)
    firstName = db.Column('firstName', db.String(30), unique=True, nullable=False)
    lastName = db.Column('lastName', db.String(30), nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    profileImg = db.Column('profileImg', db.String(20), nullable=False, default='default.jpg')
    password = db.Column('password', db.String(60), nullable=False)

    
