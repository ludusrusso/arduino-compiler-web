from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField("Qual e' il tuo nome?", validators=[Required()])
	submit = SubmitField('Ok')