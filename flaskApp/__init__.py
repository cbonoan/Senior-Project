from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 

#mysqlpwd = input("Enter password for MySQL: ")
app = Flask(__name__)
app.config['SECRET_KEY'] = '45af0f166b995f0da71012d3e6d9d708'
#uri = "mysql://admin:+" + mysqlpwd + "@flaskappdb.css4aqlso9a0.us-west-1.rds.amazonaws.com/flaskappdb"
'''
The syntax of your uri should be:
'mysql://<username>:<password>@<host>/db'

For testing purposes there will be somethings to download in order to 
create a mysql server on your localhost (i.e. 127.0.0.1)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskApp import routes