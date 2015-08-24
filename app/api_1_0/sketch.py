from . import api

from ..models import Sketch
from flask import jsonify

@api.route('/sketches/')
def get_sketches():
	sketches = Sketch.query.all()
	return jsonify({'sketches': [s.to_json() for s in sketches]})

@api.route('/sketches/<int:id>')
def get_sketch(id):
	s = Sketch.query.get_or_404(id)
	return jsonify(s.to_json())