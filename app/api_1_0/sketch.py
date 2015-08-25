from . import api

from ..models import Sketch
from .. import db
from flask import jsonify, request
from flask_json import JsonError, json_response, as_json
from datetime import datetime

from sqlalchemy.exc import IntegrityError

@api.route('/sketches/')
@as_json
def get_sketches():
	sketches = Sketch.query.all()
	return dict(sketches=[s.to_json() for s in sketches])

@api.route('/sketches/<int:id>')
@as_json
def get_sketch(id):
	s = Sketch.query.get_or_404(id)
	return s.to_json()

@api.route('/sketches/', methods=['POST'])
@as_json
def post_sketch():
	print request
	s = Sketch.from_json(request.json)
	db.session.add(s)
	try:
		db.session.commit()
	except IntegrityError:
		db.session.rollback()
		raise JsonError(error='title jet in db')
	return json_response( response='ok')

	

@api.route('/sketches/<int:id>/', methods=['DELETE'])
@as_json
def delete_sketch(id):
	s = Sketch.query.filter_by(id=id).first()
	if s is not None:
		db.session.delete(s)
		db.session.commit()
		return json_response(response='ok')
	raise JsonError(error='sketch not in database')



@api.route('/sketches/<int:id>/', methods=['PUT'])
@as_json
def put_sketch(id):
	s = Sketch.query.get_or_404(id)
	s.code = request.json.get('code', s.code)
	s.last_edit = datetime.utcnow()
	db.session.add(s)
	return json_response(response='ok')
