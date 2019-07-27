from app import db


class Pet(db.Model):
    __tablename__ = 'pet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    characteristics = db.Column(db.String(), nullable=False)

    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'characteristics': self.characteristics
        }
