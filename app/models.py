from . import db

class Sketch(db.Model):
	__tablename__ = 'Sketches'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True, index=True)
	code = db.Column(db.Text)

	def __repr__(self):
		return '<Sketch %r>' % self.title

	@staticmethod
	def from_json(json_sketch):
		title = json_post.get('title')
		code = json_post.get('code')
		return Sketch(code=code, title=title)


	def to_json(self):
		json_sketch = {
			'id' : self.id,
			'title' : self.title,
			'code' : self.code
		}
		return json_sketch
