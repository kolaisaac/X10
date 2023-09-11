from flask_sqlalchemy import SQLAlchemy

# Initialize DATABASE

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120))

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email