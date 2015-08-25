from datetime import datetime
from flask import render_template, session, redirect, url_for, request, Response

from . import ardu

from ..models import Sketch
from .. import db


@ardu.route('/') 
def index():
	s=Sketch.query.first()
	if not s:
		s = Sketch(title='template')
		db.session.add(s)
		db.session.commit()
	return render_template('ardu/arduino.html', sketch=s)

@ardu.route('/edit/<int:id>') 
def edit(id):
	s = Sketch.query.get_or_404(id)
	return render_template('ardu/arduino.html', sketch=s)


@ardu.route('/sketches') 
def sketches():
    return render_template('ardu/sketches.html', current_time=datetime.utcnow())
