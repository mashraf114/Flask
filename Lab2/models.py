from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    employees_count = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Company {self.name}>'