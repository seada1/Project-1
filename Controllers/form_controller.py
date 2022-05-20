from flask import  jsonify,request
from werkzeug.exceptions import abort

from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models.form import Form
from repositories.form_repo_impl import FormRepoImpl
from services.form_service import FormService

fr = FormRepoImpl()
fs = FormService(fr)


def route(app):
    @app.route("/forms", methods=['GET'])
    def get_all_forms():
        return jsonify([form.json() for form in fs.get_all_forms()])


    @app.route("/forms/<form_id>", methods=['GET'])
    def get_form(form_id):
        try:
            return fs.get_form(form_id).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/forms", methods=["POST"])
    def post_form():
        body = request.json

        form = Form(form_id=body["form_id"], empl_id=body["empl_id"], location=body["location"], description=body["description"], cost=body["cost"], attachment=body["attachment"], event_id=body["event_id"], grade_id=body["grade_id"], status=body["status"], award_amount=body["award_amount"] )
        form = fs.create_form(form)

        return form.json()

    @app.route("/forms/<form_id>", methods=["PUT"])
    def put_form():
        body = request.json
        form = Form(empl_id=body["empl_id"], location=body["location"], description=body["description"], cost=body["cost"], attachment=body["attachment"], event_id=body["event_id"], grade_id=body["grade_id"], status=body["status"], award_amount=body["award_amount"] )
        form = fs.update_form(form)
        return form.json()


    @app.route("/forms/<form_id>", methods=["DELETE"])
    def delete_form(form_id):
        fs.delete_form(form_id)
        return '', 204  # No Content

