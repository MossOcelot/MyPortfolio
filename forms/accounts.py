from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
    email = StringField('Input your email.')
    password = StringField('Input your password.')

    login =  SubmitField('login')

class RegisterForm(FlaskForm):
    email = StringField('Input your email.')
    password = StringField('Input your password.')
    name = StringField('Input your name.')
    surname = StringField('Input your surname')
    signup =  SubmitField('signup')

