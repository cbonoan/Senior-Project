from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskApp.models import User
from flaskApp import db

class RegistrationForm(FlaskForm):
    firstName = StringField('fname', validators=[DataRequired()])
    lastName = StringField('lname', validators=[DataRequired()])
    userName = StringField('username', 
                        validators=[DataRequired(), Length(min=5, max=20)])
    email = EmailField('email', 
                        validators=[DataRequired(), Email()])
    pwd = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Create Account')

    # Need to check if email has been used already 
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use. Please choose a different email or reset your password.')

class LoginForm(FlaskForm):
    email = EmailField('email', 
                        validators=[DataRequired(), Email()])
    pwd = PasswordField('password', validators=[DataRequired()])
    btn = SubmitField('Sign In')
    remember = BooleanField('Remember Me')

class RequestResetForm(FlaskForm):
    email = EmailField('email', 
                        validators=[DataRequired(), Email()])
    btn = SubmitField('Request Password Reset')

    # Need to check if email does not exist
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account associated with this email.')

class ResetPasswordForm(FlaskForm):
    # Have user create new password and confirm it
    pwd = PasswordField('Password', validators=[DataRequired()])
    confirmPwd = PasswordField('Confirm Password',
                                validators=[DataRequired(), EqualTo('pwd')])
    submit = SubmitField('Reset Password')
