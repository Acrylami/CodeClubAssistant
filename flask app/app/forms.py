from flask_wtf import FlaskForm, RecaptchaField
from wtforms import *
from wtforms.validators import *
#from app.models import Command

class CommandForm(FlaskForm):
    command = StringField('Command', validators=[DataRequired()])
    name = StringField('Name')
    submit = SubmitField('Submit')    
















    

