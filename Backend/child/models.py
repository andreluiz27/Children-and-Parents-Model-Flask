from main import app, db

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    parent1_id = db.Column(db.Integer, db.ForeignKey('parent.id'),
         nullable=False)
    parent2_id = db.Column(db.Integer, db.ForeignKey('parent.id'),
         nullable=False)

    def __repr__(self):
        return f"Child('{self.id}', '{self.name}')"
