from Controllers import form_controller, home_controller, employee_controller


def route(app):
    # Call all other controllers
    home_controller.route(app)
    form_controller.route(app)
    employee_controller.route(app)
