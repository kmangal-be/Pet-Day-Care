from project import app
from flask import render_template
from flask import request, jsonify
from project import db, ma

# ================================================PET-TABLE-STRUCTURE===============================================
class Pet(db.Model):
    __tablename__ = 'pet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    color = db.Column(db.String, nullable=True)
    breed = db.Column(db.String, nullable=True)
    pet_type_id = db.Column(db.Integer, db.ForeignKey('pet_type.id'))

    def __init__(self, name, age, color, breed, pet_type_id):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed
        self.pet_type_id = pet_type_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'age': self.age,
            'name': self.name,
            'color': self.color,
            'breed': self.breed,
            'pet_type_id': self.pet_type_id
        }

# ==============================================Response-Class===========================================================
class PetSchema(ma.Schema):
    class Meta:
        # fields to expose
        fields = ('age', 'name', 'color', 'breed', 'pet_type_id')

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)


# ===============================================APIS===================================================================

# Pet Creation
@app.route('/pet', methods=['POST'])
def create():
    data = request.get_json(force=True)
    new_pet = Pet(data)
    db.session.add(new_pet)
    db.session.commit()
    return jsonify({'status': 200, "data": data})


# Get All Pets
@app.route('/pet', methods=['GET'])
def get_all_pet():
    all_pets = Pet.query.all()
    result = pets_schema.dump(all_pets)
    return jsonify(result.data)


# Get Specific Pet
@app.route("/pet/<id>", methods=['GET'])
def pet_detail(id):
    pet = Pet.query.get(id)
    return pet_schema.jsonify(pet)
