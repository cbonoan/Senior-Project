from flask import render_template, url_for, flash, redirect, request, session, g
from flaskApp import app, db
from flaskApp.forms import *
from flaskApp.models import *


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@app.route("/meditation")
def meditation():
    return render_template('meditation.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = None
        try:
            user = User(form.firstName.data, form.lastName.data, form.userName.data, form.email.data, form.pwd.data)
        except TypeError as e: 
            print(e)
        
        if user:
            flash(f'Account created for {form.userName.data}!', 'success')
            return redirect(url_for('login'))
        elif user is None:
            flash(f'Error creating account for {form.userName.data}.', 'danger')
            return redirect(url_for('register'))
    
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('login.html', title='Login', form=form)

