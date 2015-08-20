from datetime import datetime
from flask import render_template, session, redirect, url_for, request, Response

from . import ardu

@ardu.route('/') 
def index():
	return render_template('ardu/arduino.html')

@ardu.route('/_compile')
def compile():
    from .compiler import Compiler
    comp = Compiler();
    prog = request.args.get('prog', 0, type=str)
    comp.save(prog)
    comp.compile()
    return Response(comp.read_proc(), mimetype='text/event-stream')

@ardu.route('/_monitor')
def compile():
    from .compiler import Compiler
    comp = Compiler();
    comp.monitor()
    return Response(comp.read_proc(), mimetype='text/event-stream')