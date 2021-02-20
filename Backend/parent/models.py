from main import app, db
from child.models import Child

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    child = db.relationship('Child', backref='parent', lazy=True)

    def __repr__(self):
        return f"Parent('{self.id}', '{self.name}')"


