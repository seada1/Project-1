from flask import jsonify, request
from exceptions.resource_not_found import ResourceNotFound
from repositories.employee_repo_impl import EmployeeRepoImpl
from services.employee_services import EmployeeService
from models.employee import Employee

er = EmployeeRepoImpl()
es = EmployeeService(er)


def route(app):
    @app.route("/forms/<form_id>/employees", methods=["GET"])
    def get_employees_from_form(form_id):

        return jsonify([employee.json() for employee in es.all_employees_in_form(form_id)])

    @app.route("/employees", methods=["GET"])
    def get_all_employees():

        return jsonify([employee.json() for employee in es.get_all_employees()])

    @app.route("/employees/<empl_id>", methods=['GET'])
    def get_employee(empl_id):
        try:
            return es.get_employee(int(empl_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees", methods=["POST"])
    def post_employee():
        body = request.json

        employee = Employee(empl_id=body["empl_id"], fname=body["fname"], lname=body["lname"],gender=body["gender"], email=body["email"], phone=body["phone"], position=body["position"], address=body["address"], user_id=body["user_id"], password=body["password"])
        employee = es.create_employee(employee)

        return employee.json()

    @app.route("/employees/<empl_id>", methods=["DELETE"])
    def del_employee(empl_id):
        es.delete_employee(empl_id)
        return '', 204  # No Content

    @app.route("/employees/<empl_id>", methods=["PUT"])
    def put_employee():
        body = request.json

        employee = Employee(empl_id=body["empl_id"], fname=body["fname"], lname=body["lname"],gender=body["gender"], email=body["email"], phone=body["phone"], position=body["position"], address=body["address"], user_id=body["user_id"], password=body["password"])
        employee = es.update_employee(employee)

        return employee.json()
