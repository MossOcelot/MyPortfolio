from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class ProfileDetailFrom(FlaskForm):
    name = StringField('Input your name and surname.')
    age = IntegerField('Input your age.')
    experience = IntegerField('Input your experience.')
    phone = StringField('Input your phone.')
    email = StringField('Input your email.')
    degree = StringField('Input your degree.')
    fax = StringField('Input your fax.')
    website = StringField('Input your website.')
    careerlevel = StringField('Input your careerlevel')

    submit = SubmitField('submit')
