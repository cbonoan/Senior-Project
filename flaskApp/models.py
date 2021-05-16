# Use these classes to insert into database schemas 
from flaskApp import db, login_manager, app
from random import randint
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import INTEGER
from datetime import date
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Admin(db.Model, UserMixin):
    adminid = db.Column(INTEGER(unsigned=True), nullable=False, unique=True)
    id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, unique=True)
    userid = db.Column(INTEGER(unsigned=True), db.ForeignKey('user.id'))
    
class User(db.Model, UserMixin):
    id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, unique=True)
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(65), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    feelingsId = db.relationship("Feelings")

    # This function is to help users reset their password
    def getResetToken(self, expiresSec=1800):
        s = Serializer(app.config['SECRET_KEY'], expiresSec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    # Verify the token given to user to reset password
    @staticmethod
    def verifyResetToken(token):
        s = Serializer(app.config['SECRET_KEY'])
        # Check if the token is expired 
        try:
            userId = s.loads(token)['user_id']
        except:
            return None
        
        return User.query.get(userId)
    
class Feelings(db.Model, UserMixin):
    id = db.Column(INTEGER(unsigned=True), db.ForeignKey('user.id'), unique=True, nullable=False, primary_key=True)
    emotion = db.Column(db.String(45), nullable=False, primary_key=True)
    date = db.Column(db.Date, nullable=False, primary_key=True)

# Rest of classes are for recommending user based on feeling 
class Games(db.Model, UserMixin):
    games_emotion = db.Column(db.String(45), nullable=False, primary_key=True)
    games_title = db.Column(db.String(45), nullable=False, primary_key=True)

class Movies(db.Model, UserMixin):
    movie_emotion = db.Column(db.String(45), nullable=False, primary_key=True)
    movie_title = db.Column(db.String(45), nullable=False, primary_key=True)

class Songs(db.Model, UserMixin):
    songs_emotion = db.Column(db.String(45), nullable=False, primary_key=True)
    songs_title = db.Column(db.String(45), nullable=False, primary_key=True)

class Articles(db.Model, UserMixin):
    article_emotion = db.Column(db.String(45), nullable=False, primary_key=True)
    article_title = db.Column(db.String(45), nullable=True, default=None)

class Book(db.Model, UserMixin):
    book_emotion = db.Column(db.String(45), nullable=False, primary_key=True)
    book_title = db.Column(db.String(45), nullable=True, primary_key=True)