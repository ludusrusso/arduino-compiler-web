from datetime import datetime
from flask import render_template, session, redirect, url_for, request, Response

from . import ardu

from .compiler import Compiler

from ..models import Sketch
from .. import db

comp = Compiler();

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


@ardu.route('/_compile')
def compile():
    prog = request.args.get('prog', 0, type=str)
    comp.save(prog)
    comp.compile()
    return Response(comp.read_proc(), mimetype='text/event-stream')

@ardu.route('/_start_monitor')
def start_monitor():
    baud = request.args.get('baud', 9600, type=int)
    return Response(comp.monitor_open(baud=baud), mimetype='text/event-stream')

@ardu.route('/_stop_monitor')
def stop_monitor():
    comp.monitor_close();
    return "redirect(ardu.route)"