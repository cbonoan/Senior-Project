from flask import render_template, url_for, flash, redirect, request, session, g
from flaskApp import app, db, bcrypt
from flaskApp.forms import *
from flaskApp.models import *
from flask_login import login_user, logout_user, current_user, login_required
from random import randint
from flask_session import Session

app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/quiz")
@login_required
def quiz():
    return render_template('quiz.html', title='Quiz')

@app.route("/results")
def results():
    return render_template('results.html')

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

@app.route("/settings", methods=['GET','POST'])
@login_required
def settings():
    email = current_user.email
    username = current_user.username
    name = current_user.name
    number = randint(100000,999999)
    session['number'] = number
    return render_template('settings.html', title=current_user.username + "'s Settings", email = email, username = username, name = name, number = number )

@app.route("/settings_post", methods=['GET','POST'])
@login_required
def settings_post():    
    if request.method == 'POST':
        form = request.form
        
        if str(session.get('number')) == request.form['rand_number'].strip():
            if request.form['password1'] != "" and request.form['password'] != "" and bcrypt.check_password_hash(current_user.password, request.form['password']) and (request.form['password1'] == request.form['password2']):
                hashed_pwd = bcrypt.generate_password_hash(request.form['password1']).decode('utf-8')
                current_user.password = hashed_pwd
                db.session.commit()
            elif (request.form['password'] != "") or (request.form['password1'] != "") or (request.form['password2'] != ""):
                flash(f'Insufficient password information, settings not saved.', 'success')
                return redirect(url_for('home'))
            if request.form['email'].strip() != current_user.email:
                current_user.email = request.form['email'].strip()
                db.session.commit()
            if request.form['username'].strip() != current_user.username:
                current_user.username = request.form['username'].strip()
                db.session.commit()
            if request.form['name'].strip() != current_user.name:
                current_user.name = request.form['name'].strip()
                db.session.commit()    
            
            flash(f'Settings successfully saved.', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Incorrect confirmation number, settings not saved.', 'success')
            return redirect(url_for('home'))
    return redirect(url_for('home'))

@app.route("/calendar")
@login_required
def calendar():
    email = current_user.email
    feeling = Feelings.query.filter_by(id=current_user.id).all()
    print(len(feeling))
    return render_template('calendar.html', email=email, feeling=feeling, size = len(feeling))

