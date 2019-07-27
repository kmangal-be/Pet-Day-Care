from app import db


class Pet(db.Model):
    __tablename__ = 'pet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=True)
    breed = db.Column(db.String, nullable=True)
    pet_type_id = db.Column(db.Integer, db.ForeignKey('pet_type.id'))

    def __init__(self, name, color, breed, pet_type_id):
        self.name = name
        self.color = color
        self.breed = breed
        self.pet_type_id = pet_type_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'breed': self.breed,
            'pet_type_id': self.pet_type_id
        }


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    mobile_no = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    emergency_mobile_no = db.Column(db.String, nullable=True)
    dob = db.Column(db.String, nullable=True)
    #Have to replace with date type
    hire_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __init__(self, name, mobile_no, address, emergency_mobile_no, dob, hire_date, end_date):
        self.name = name
        self.mobile_no = mobile_no
        self.address = address
        self.emergency_mobile_no = emergency_mobile_no
        self.dob = dob
        self.hire_date = hire_date
        self.end_date = end_date

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile_no': self.mobile_no,
            'address': self.address,
            'emergency_mobile_no': self.emergency_mobile_no,
            'dob': self.emergency_mobile_no,
            'hire_date': self.hire_date,
            'end_date': self.end_date
        }


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    mobile_no = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=True)

    def __init__(self, name, mobile_no, address, emergency_mobile_no, dob, hire_date, end_date):
        self.name = name
        self.mobile_no = mobile_no
        self.address = address
        self.dob = dob


    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile_no': self.mobile_no,
            'address': self.address,
            'dob': self.emergency_mobile_no,
        }



class PetType(db.Model):
    __tablename__ = 'pet_type'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False),
    size = db.Column(db.String, nullable=False),
    points = db.Column(db.Integer, nullable=False),

    def __init__(self, id, type, size, points):
        self.id = id
        self.type = type
        self.size = size
        self.points = points

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.type,
            'color': self.size,
            'breed': self.points
        }


class Bookings(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False, db.ForeignKey('customer.id'))
    employee_id = db.Column(db.Integer, nullable=False, db.ForeignKey('employee.id'))
    pet_id = db.Column(db.Integer, nullable=False, db.ForeignKey('pet.id'))
    points = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)


    def __init__(self, id, customer_id, employee_id, pet_id, points, amount):
        self.id = id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.pet_id = pet_id
        self.points = points
        self.amount = amount

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'customer_id': self.type,
            'employee_id': self.size,
            'pet_id': self.pet_id,
            'points': self.points,
            'amount': self.amount
        }


class Payments(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'))
    payment_status = db.Column(db.String, nullable=False)
    payment_mode = db.Column(db.String, nullable=False)



    def __init__(self, id, booking_id, payment_status, payment_mode):
        self.id = id
        self.booking_id = customer_id
        self.payment_status = payment_status,
        self.payment_mode = payment_mode

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'booking_id': self.booking_id,
            'payment_status': self.payment_status,
            'payment_mode': self.payment_mode
        }
