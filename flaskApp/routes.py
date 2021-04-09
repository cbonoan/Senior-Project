from flask import render_template, url_for, flash, redirect, request, session, g
from flaskApp import app, db, bcrypt
from flaskApp.forms import *
from flaskApp.models import *
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/quiz")
def quiz():
    if current_user.is_authenticated:
        return render_template('quiz.html')
    
    form = LoginForm()
    flash("Please login or create an account first!", 'warning')
    return redirect(url_for('login'))

@app.route("/meditation")
def meditation():
    return render_template('meditation.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated: 
        return redirect(url_for('home'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        fullName = form.firstName.data + " " + form.lastName.data
        #Generate 5 digit userid 
        uid = ""
        for i in range(5):
            uid += str(randint(0,9))
        hashed_pwd = bcrypt.generate_password_hash(form.pwd.data).decode('utf-8') # bcrypt will be used to encrypt user passwords
        user = User(id=uid, username=form.userName.data, email=form.email.data, password=hashed_pwd, name=fullName)
        if user:
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.userName.data}!', 'success')
            return redirect(url_for('login'))
        elif user is None:
            flash(f'Error creating account for {form.userName.data}.', 'danger')
            return redirect(url_for('register'))
    
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.pwd.data):
            login_user(user, remember=form.remember.data)
            # Next line sees if a user was trying to access a page before needing to login 
            # Allows user to be redirected to page they want instead of going back to home page
            requestedPage = request.args.get('next')
            print(requestedPage)
            if requestedPage: 
                return redirect(requestedPage)
            else:
                flash(f'Welcome back, {user.username}!', 'success')
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', title=current_user.username + "'s Profile")

