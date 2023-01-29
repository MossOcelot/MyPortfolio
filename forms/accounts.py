from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, validators

class LoginForm(FlaskForm):
    email = StringField(
        "name", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    password = PasswordField(
        "password",
        validators=[
            validators.DataRequired(),
            validators.Length(min=3, message="มากกว่า 3"),
        ],
    )

    login =  SubmitField('login')

class RegisterForm(FlaskForm):
    email = StringField('Input your email.')
    password = StringField('Input your password.')
    name = StringField('Input your name.')
    surname = StringField('Input your surname')
    signup =  SubmitField('signup')

