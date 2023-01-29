from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField,validators

class ProfileDetailFrom(FlaskForm):
    name = StringField('Input your name and surname.',validators=[validators.DataRequired()])
    age = IntegerField('Input your age.')
    experience = IntegerField('Input your experience.')
    phone = StringField('Input your phone.')
    email = StringField('Input your email.',
    validators=[validators.DataRequired(), validators.Length(min=3)])
    degree = StringField('Input your degree.')
    fax = StringField('Input your fax.')
    website = StringField('Input your website.')
    careerlevel = StringField('Input your careerlevel')

    submit = SubmitField('submit')
