from repositories.employee_repo import EmployeeRepo


class EmployeeService:

    def __init__(self, employee_repo: EmployeeRepo):
        self.employee_repo = employee_repo

    def all_employees_in_form(self, form_id):
        return self.employee_repo.get_employees_from_form(form_id)

    def get_employees_from_form(self, empl_id, form_id):
        pass

    def create_employee(self, employee):
        return self.employee_repo.create_employee(employee)

    def get_employee(self, empl_id):
        return self.employee_repo.get_employee(empl_id)

    def get_all_employees(self):
        return self.employee_repo.get_all_employees()

    def update_employee(self, change):
        return self.employee_repo.update_employee(change)

    def delete_employee(self, empl_id):
        return self.employee_repo.delete_employee(empl_id)
