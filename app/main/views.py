from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm 
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST']) 
def index():
	user = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		user = User.query.filter_by(username=name).first()
		if user == None:
			user = User(username=name)
		form.name.data = ''
	return render_template('index.html', current_time=datetime.utcnow(), form=form, user=user)
