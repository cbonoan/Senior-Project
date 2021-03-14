from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    firstName = StringField('fname', validators=[DataRequired()])
    lastName = StringField('lname', validators=[DataRequired()])
    userName = StringField('username', 
                        validators=[DataRequired(), Length(min=5, max=20)])
    email = EmailField('email', 
                        validators=[DataRequired(), Email()])
    pwd = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = EmailField('email', 
                        validators=[DataRequired(), Email()])
    pwd = PasswordField('password', validators=[DataRequired()])
    btn = SubmitField('Sign In')
    remember = BooleanField('Remember Me')

    