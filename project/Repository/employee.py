from project import app
from flask import render_template
from flask import request, jsonify
from project import db, ma
import datetime


# ================================================EMPLOYEE-TABLE-STRUCTURE===============================================
class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    mobile_no = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    emergency_mobile_no = db.Column(db.String)
    dob = db.Column(db.String, nullable=True)
    # Have to replace with date type
    hire_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)

    def __init__(self, data):
        self.name = data['name']
        self.mobile_no = data['mobile_no']
        self.address = data['address']
        self.emergency_mobile_no = data.get('emergency_mobile_no', None)
        self.dob = data['dob']
        self.hire_date = data['hire_date']
        self.end_date = data.get('end_date', None)

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


# ==============================================Response-Class===========================================================
class EmployeeSchema(ma.Schema):
    class Meta:
        # fields to expose
        fields = ('name', 'mobile_no', 'address', 'emergency_mobile_no', 'dob', 'hire_date', 'end_date')


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


# ===============================================APIS===================================================================

# Employee On-boarding
@app.route('/employee', methods=['POST'])
def create():
    data = request.get_json(force=True)
    new_employee = Employee(data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'status': 200, "data": data})


# Get All Employees
@app.route('/employee', methods=['GET'])
def get_all_employee():
    all_employees = Employee.query.all()
    result = employees_schema.dump(all_employees)
    return jsonify(result.data)


# Get Specific Employee
@app.route("/employee/<id>", methods=['GET'])
def employee_detail(id):
    employee = Employee.query.get(id)
    return employee_schema.jsonify(employee)


# Update Specific Employee
@app.route("/employee/<id>", methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    end_date = request.json['end_date']
    if employee.end_date is None:
        employee.end_date = end_date
    db.session.commit()
    return employee_schema.jsonify(employee)


@app.errorhandler(404)
def page_not_found(e):
    return "This Page was not found"
