from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    pass

class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Length(min=3, max=20)])                        
    password = PasswordField(validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    