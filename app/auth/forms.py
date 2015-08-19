from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from wtforms.validators import Required, Email

class LoginForm(Form):
    email = StringField('User Name', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')