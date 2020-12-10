from flask import render_template, url_for, flash, redirect, request, session, g
from flaskApp import app, db
from flaskApp.forms import *
from flaskApp.models import *


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        register = request.form
        firstName = register['firstName']
        lastName = register['lastName']
        email = register['email']
        password = register['pwd']

        user = User(firstName=firstName, lastName=lastName, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', title='Register')

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('login.html', title='Login')