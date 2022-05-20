from abc import ABC

from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from repositories.employee_repo import EmployeeRepo
from util.db_connection import connection


# Helper Function
def _build_employee(record):
    return Employee(empl_id=record[0], fname=record[1], lname=record[2],gender=record[3], email=record[4], phone=record[5], position=record[6], address=record[7], user_id=record[8], password=record[9])


class EmployeeRepoImpl(EmployeeRepo, ABC):

    def create_employee(self, employee):
        sql = "INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [employee.empl_id, employee.fname, employee.lname, employee.gender, employee.email, employee.phone, employee.position, employee.address, employee.user_id, employee.password])

        connection.commit()
        record = cursor.fetchone()

        return _build_employee(record)

    def get_employee(self, empl_id):
        sql = "SELECT * FROM employees WHERE empl_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [empl_id])

        record = cursor.fetchone()

        if record:
            return _build_employee(record)
        else:
            raise ResourceNotFound(f"Employee with id: {empl_id} - Not Found")

    def get_all_employees(self):
        sql = "SELECT * FROM employees"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        return [_build_employee(record) for record in records]

    def update_employee(self, change):
        sql = "UPDATE employee SET fname =%s, lname=%s, gender=%s, email=%s, phone=%s,  position=%s,address=%s, user_id=%s, password=%s, WHERE empl_id = %s  " \
              "RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.fname, change.lname, change.gender, change.email, change.phone, change.position, change.address, change.user_id, change.password])

        connection.commit()
        record = cursor.fetchone()

        return _build_employee(record)

    def delete_employee(self, empl_id):
        sql = "DELETE FROM employees WHERE empl_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [empl_id])
        connection.commit()

    def get_employees_from_form(self, form_id):
        sql = "SELECT employees.* FROM EmployeeForm " \
              "LEFT JOIN employees ON EmployeeForm.empl_id = employees.empl_id " \
              "WHERE EmployeeForm.form_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [form_id])

        records = cursor.fetchall()
        return [_build_employee(record) for record in records]


def _test():
    er = EmployeeRepoImpl()
    print(er.get_employee(202))
    print(er.get_all_employees())



if __name__ == '__main__':
    _test()


