from flask import render_template, url_for, flash, redirect, request, session, g, jsonify
from flaskApp import app, db, bcrypt, mail
from flaskApp.forms import *
from flaskApp.models import *
from flask_login import login_user, logout_user, current_user, login_required
from random import randint
from flask_session import Session
from flask_mail import Message
import json

app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Global variables here if needed 

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/quiz")
@login_required
def quiz():
    return render_template('quiz.html', title='Quiz')

@app.route("/results", methods=['GET','POST'])
@login_required
def results():
    if request.method == 'POST':
        emotion_temp = ""
        neutral = {
            -0.5: "bored", -0.4: "indifferent", -0.3: "apathetic", -0.2: "distant", -0.1: "reserved", 
            0.0: "independent", 0.1: "relaxed", 0.2: "calm", 0.3: "sleepy", 0.4: "content", 0.5: "satisfied"
        }
        good = {
            0.5: "joyful", 0.6: "amused", 0.7: "inspired", 0.8: "confident", 0.9: "recreational",
            1.0: "reminiscent", 1.1: "creative", 1.2: "enthusiastic", 1.3: "self-assured", 1.4: "playful",
            1.5: "nostalgic", 1.6: "artistic", 1.7: "passionate", 1.8: "valued", 1.9: "curious", 2.0: "thankful"
         }
        bad = {
            -2.0: "skeptical", -1.9: "bitter", -1.8: "paranoid", -1.7: "worthless", -1.6: "embarrassed", -1.5: "abandoned",
            -1.4: "annoyed", -1.3: "fearful", -1.2: "hopeless", -1.1: "powerless", -1.0: "lonely",
            -0.9: "frustrated", -0.8: "scared", -0.7: "worried", -0.6: "vulnerable", -0.5: "melancholy"
        }
        if(float(request.form['avg']) <= -0.5):
            emotion_temp = bad[float(request.form['avg'])]
        elif(float(request.form['avg']) <= 0.5):
            emotion_temp = neutral[float(request.form['avg'])]
        else:
            emotion_temp = good[float(request.form['avg'])]

        check = Feelings.query.filter_by(id=current_user.id, date=date.today()).first()
        articles = Articles.query.filter_by(article_emotion = emotion_temp).first()
        songs = Songs.query.filter_by(songs_emotion = emotion_temp).first()
        books = Book.query.filter_by(book_emotion=emotion_temp).first()
        #print(check)
        if check:
            check.emotion = emotion_temp
            db.session.commit()
        else:
            feelings = Feelings(id=current_user.id, emotion= emotion_temp,date=date.today())
            db.session.add(feelings)
            db.session.commit()
        #print(date.today())
        return render_template('results.html',article=articles.article_title,song=songs.songs_link,book=books.book_title, emotion=emotion_temp)
    return render_template('index.html')

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
    print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
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

def sendResetEmail(user):
    token = user.getResetToken()
    msg = Message('Password Reset Request', 
                sender="noreply@mindsanctuary.com", 
                recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('resetToken', token=token, _external=True)}

If you did not request a password reset, then please ignore this email and no changes will be made.
'''
    mail.send(msg)


@app.route("/reset_password", methods=['GET','POST'])
def resetRequest():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RequestResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if(user is None):
            flash("There is noaccount associated with this email.", 'warning')
            return redirect(url_for('register'))

        sendResetEmail(user)
        flash("Please check your email to reset your password.", 'info')
        return redirect(url_for('login'))

    return render_template('resetRequest.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET','POST'])
def resetToken(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    user = User.verifyResetToken(token)
    if user is None:
        flash("Token is invalid or has expired", 'warning')
        return redirect(url_for('resetRequest'))
    
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.pwd.data).decode('utf-8')
        user.password = hashed_pwd
        db.session.commit()
        flash(f'Your password has been updated!', 'success')
        return redirect(url_for('login'))
    return render_template('resetToken.html', title='Reset Password', form=form)

    
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
                flash(f'Insufficient password information, settings not saved.', 'warning')
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
            flash(f'Incorrect confirmation number, settings not saved.', 'warning')
            return redirect(url_for('home'))
    return redirect(url_for('home'))

@app.route("/calendar")
@login_required
def calendar():
    email = current_user.email
    feeling = Feelings.query.filter_by(id=current_user.id).all()

    return render_template('calendar.html', email=email, feeling=feeling, size = len(feeling))