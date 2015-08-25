from . import api

from ..models import Sketch
from .. import db
from flask import jsonify, request


@api.route('/sketches/')
def get_sketches():
	sketches = Sketch.query.all()
	return jsonify({'sketches': [s.to_json() for s in sketches]})

@api.route('/sketches/<int:id>')
def get_sketch(id):
	s = Sketch.query.get_or_404(id)
	return jsonify(s.to_json())

@api.route('/sketches/', methods=['POST'])
def post_sketch():
	print request
	s = Sketch.from_json(request.json)
	db.session.add(s)
	db.session.commit()
	return jsonify(s.to_json())

@api.route('/sketches/<int:id>/', methods=['DELETE'])
def delete_sketch(id):
	s = Sketch.query.filter_by(id=id).first()
	if s is not None:
		db.session.delete(s)
		db.session.commit()
		return jsonify(s.to_json())
	return '404'
