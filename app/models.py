from . import db
from datetime import datetime

class Sketch(db.Model):
	__tablename__ = 'Sketches'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True, index=True)
	code = db.Column(db.Text, default="void setup() {\n}\n\nvoid loop() {\n\n}")
	last_edit = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Sketch %r>' % self.title

	@staticmethod
	def from_json(json_sketch):
		title = json_sketch.get('title')
		code = json_sketch.get('code')
		return Sketch(code=code, title=title)


	def to_json(self):
		json_sketch = {
			'id' : self.id,
			'title' : self.title,
			'code' : self.code,
			'last_edit' : self.last_edit
		}
		return json_sketch
