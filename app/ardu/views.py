from datetime import datetime
from flask import render_template, session, redirect, url_for, request, Response

from . import ardu

from .compiler import Compiler
comp = Compiler();

@ardu.route('/') 
def index():
	return render_template('ardu/arduino.html')

@ardu.route('/_compile')
def compile():
    prog = request.args.get('prog', 0, type=str)
    comp.save(prog)
    comp.compile()
    return Response(comp.read_proc(), mimetype='text/event-stream')

@ardu.route('/_start_monitor')
def start_monitor():
	baud = request.args.get('baud', 9600, type=int)
	print baud
    return Response(comp.monitor_open(baud=baud), mimetype='text/event-stream')

@ardu.route('/_stop_monitor')
def stop_monitor():
    comp.monitor_close();
    return "redirect(ardu.route)"