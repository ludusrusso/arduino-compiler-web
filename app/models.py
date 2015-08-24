from . import db

class Sketch(db.Model):
	__tablename__ = 'Sketches'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True, index=True)
	code = db.Column(db.Text)

	def __repr__(self):
		return '<Sketch %r>' % self.title