from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

import os   # This is needed to store secret information like server password for db

app = Flask(__name__)
app.config['SECRET_KEY'] = '45af0f166b995f0da71012d3e6d9d708' # Protects application from certain attacks

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:"+os.environ.get('DB_PWD')+"@127.0.0.1:3307/devdb"
db = SQLAlchemy(app) 

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # If user is trying to access a page that requires them to login, they will be redirected to the login page
login_manager.login_message_category = 'info'

from flaskApp import routes