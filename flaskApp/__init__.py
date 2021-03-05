from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt 
import os   # This is needed to store secret information like server password

#mysqlpwd = input("Enter password for MySQL: ")
app = Flask(__name__)
app.config['SECRET_KEY'] = '45af0f166b995f0da71012d3e6d9d708'
#uri = "mysql://admin:+" + mysqlpwd + "@flaskappdb.css4aqlso9a0.us-west-1.rds.amazonaws.com/flaskappdb"
'''
The syntax of your uri should be:
'mysql://<username>:<password>@<host>/db'

For testing purposes there will be somethings to download in order to 
create a mysql server on your localhost (i.e. 127.0.0.1)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
'''
# Connecting to MySQL server 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PWD')
app.config['MYSQL_HOST'] = 'localhost'
# Comment out next line if test db sits on default port
app.config['MYSQL_PORT'] = '3307'
# Change db name to match the name you used 
app.config['MYSQL_DB'] = 'devdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = MySQL(app)

bcrypt = Bcrypt(app)

from flaskApp import routes