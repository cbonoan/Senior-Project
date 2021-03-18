# Use these classes to insert into database schemas 
from flaskApp import db, login_manager
from random import randint
from flask_login import UserMixin
from datetime import date

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Admin(db.Model, UserMixin):
    adminid = db.Column(db.Integer, nullable=False, unique=True)
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, auto_increment=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, auto_increment=True)
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(65), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    
class Feelings(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    emotion = db.Column(db.String(45), nullable=False, primary_key=True)
    date = db.Column(db.Date, nullable=False, primary_key=True, default=date.today().strftime("%Y-%m-%d"))
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Rest of classes are for recommending user based on feeling 
class Games(db.Model, UserMixin):
    games_emotion = db.Column(db.String(45), db.ForeignKey('feelings.emotion'), nullable=False, primary_key=True)
    games_title = db.Column(db.String(45), nullable=False, primary_key=True)

class Movies(db.Model, UserMixin):
    movie_emotion = db.Column(db.String(45), db.ForeignKey('feelings.emotion'), nullable=False, primary_key=True)
    movie_title = db.Column(db.String(45), nullable=False, primary_key=True)

class Songs(db.Model, UserMixin):
    songs_emotion = db.Column(db.String(45), db.ForeignKey('feelings.emotion'), nullable=False, primary_key=True)
    songs_title = db.Column(db.String(45), nullable=False, primary_key=True)

class Articles(db.Model, UserMixin):
    article_emotion = db.Column(db.String(45), db.ForeignKey('feelings.emotion'), nullable=False, primary_key=True)
    article_title = db.Column(db.String(45), nullable=True, default=None)

class Book(db.Model, UserMixin):
    book_emotion = db.Column(db.String(45), db.ForeignKey('feelings.emotion'), nullable=False, primary_key=True)
    book_title = db.Column(db.String(45), nullable=True, primary_key=True)

class Excercises(db.Model, UserMixin):
    excercises_emotion = db.Column(db.String(45), db.ForeignKey('feelings.emotion'), nullable=False, primary_key=True)
    excercises_title = db.Column(db.String(45), nullable=True, primary_key=True)

