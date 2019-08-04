from project import db

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
    type = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    points = db.Column(db.Integer, nullable=False)

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
            'type': self.type,
            'size': self.size,
            'points': self.points
        }


class Bookings(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    start_time_stamp = db.Column(db.String, nullable=False)
    end_time_stamp = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))

    def __init__(self, id, customer_id, employee_id, pet_id, points, amount, start_time_stamp, end_time_stamp):
        self.id = id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.pet_id = pet_id
        self.points = points
        self.amount = amount
        self.start_time_stamp = start_time_stamp
        self.end_time_stamp = end_time_stamp

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'customer_id': self.type,
            'employee_id': self.size,
            'pet_id': self.pet_id,
            'points': self.points,
            'amount': self.amount,
            'start_time_stamp': self.start_time_stamp,
            'end_time_stamp': self.end_time_stamp
        }


class Payments(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'))
    payment_status = db.Column(db.String, nullable=False)
    payment_mode = db.Column(db.String, nullable=False)

    def __init__(self, id, booking_id, payment_status, payment_mode):
        self.id = id
        self.booking_id = booking_id
        self.payment_status = payment_status
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
