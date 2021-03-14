from flask import Flask
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt 
import os   # This is needed to store secret information like server password for db

app = Flask(__name__)
app.config['SECRET_KEY'] = '45af0f166b995f0da71012d3e6d9d708' # Protects application from certain attacks

# Connecting to MySQL server 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PWD')
# Comment out next line if test db sits on default port
app.config['MYSQL_PORT'] = 3307
# Change db name to match the name you used 
app.config['MYSQL_DB'] = 'devdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
db = MySQL(app)





bcrypt = Bcrypt(app)

from flaskApp import routes