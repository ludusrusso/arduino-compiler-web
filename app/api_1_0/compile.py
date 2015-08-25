from . import api
from ..models import Sketch
from compiler import Compiler

from flask_json import JsonError, json_response
from flask import Response, request

comp = Compiler();


@api.route('/monitor')
def start_monitor():
    req = request.args.get('monitor', 'stop', type=str)
    if req == 'start':
        baud = request.args.get('baud', 9600, type=int)
        if comp.monitor_open(baud=baud):
            return Response(comp.read_monitor(), mimetype='text/event-stream')
        raise JsonError(error='resource busy')
    elif req == 'stop':
        comp.monitor_close();
        return json_response( response='ok')
    else:
        raise JsonError(error='bad request')

@api.route('/compile/<int:id>/')
def compile(id):
    s = Sketch.query.get_or_404(id)
    comp.save(s.code)
    comp.compile()
    return Response(comp.read_proc(), mimetype='text/event-stream')

