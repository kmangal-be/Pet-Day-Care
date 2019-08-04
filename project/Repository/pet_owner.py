from project import app
from flask import render_template
from flask import request, jsonify
from project import db, ma

# ================================================PET-OWNER-TABLE-STRUCTURE===============================================
class PetOwner(db.Model):
    __tablename__ = 'pet_owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    mobile_no = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=True)

    def __init__(self, data):
        self.name = data['name']
        self.mobile_no = data['mobile_no']
        self.address = data['address']
        self.dob = data['dob']

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile_no': self.mobile_no,
            'address': self.address,
            'dob': self.dob
        }


# ==============================================Response-Class===========================================================
class PetOwnerSchema(ma.Schema):
    class Meta:
        # fields to expose
        fields = ('name', 'mobile_no', 'address', 'dob' )


pet_owner_schema = PetOwnerSchema()
pet_owners_schema = PetOwnerSchema(many=True)


# ===============================================APIS===================================================================

# PetOwner Creation
@app.route('/pet-owner', methods=['POST'])
def create_pet_owner():
    data = request.get_json(force=True)
    new_pet_owner = PetOwner(data)
    db.session.add(new_pet_owner)
    db.session.commit()
    return jsonify({'status': 200, "data": data})


# Get All Pet Owners
@app.route('/pet-owner', methods=['GET'])
def get_all_pet_owners():
    all_pet_owner = PetOwner.query.all()
    result = pet_owner_schema.dump(all_pet_owner)
    return jsonify(result.data)


# Get Specific Pet Owner
@app.route("/pet-owner/<id>", methods=['GET'])
def get_pet_owner_detail(id):
    pet_owner = PetOwner.query.get(id)
    return pet_owner_schema.jsonify(pet_owner)


