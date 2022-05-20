from abc import ABC

from exceptions.resource_not_found import ResourceNotFound
from models.form import Form
from repositories.form_repo import FormRepo
from util.db_connection import connection


# Helper Method
def _build_form(record):
    if record:
        return Form(form_id=record[0], empl_id=record[1], location=record[2], description=record[3], cost=record[4], attachment=record[5], event_id=record[6], grade_id=record[7], status=record[8], award_amount=record[9])
    else:
        return None

class FormRepoImpl(FormRepo, ABC):

    def create_form(self, form):
        sql = "INSERT INTO forms VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [form.form_id, form.empl_id, form.location, form.description, form.cost, form.attachment, form.event_id, form.grade_id, form.status, form.award_amount])

        connection.commit()
        record = cursor.fetchone()

        return _build_form(record)

    def get_form(self, form_id):

        sql = "SELECT * FROM forms WHERE form_id= %s"
        cursor = connection.cursor()

        cursor.execute(sql, [form_id])

        record = cursor.fetchone()

        if record:
            return _build_form(record)
        else:
            raise ResourceNotFound(f"Form with number: {form_id} - Not Found")

    def get_all_forms(self):
        sql = "SELECT * FROM forms"
        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        # form_list = [_build_form(record) for record in records]
        #
        # return form_list
        return [_build_form(record) for record in records]


    def get_status(self, form_id):
        sql = "SELECT status FROM forms WHERE form_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [form_id])
        record = cursor.fetchone()
        status = record[0]
        if record:
            return status
        else:
            print("pending")
            #raise ResourceNotFound(f"Status with form id: {form_id} - Not Found")


    def update_form(self, change):
        sql = "UPDATE forms SET form_id =%s, empl_id=%s, location=%s, description=%s, cost=%s,  attachment=%s,event_id=%s, grade_id=%s, status=%s, award_amount=%s, WHERE form_id = %s  " \
              "RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.account_type, change.current_balance, change.client_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_form(record)

    def delete_form(self, form_id):
        sql = "DELETE FROM forms WHERE form_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [form_id])
        connection.commit()

def _test():

    fr = FormRepoImpl()
    form = fr.get_form(101)
    print(form)

    print(fr.get_all_forms())


    # form = Form(form_id="f05", empl_id="e03", location="location 3", description="description 3", cost=500, attachment="", event_id="v04", grade_id="g03", status="not awarded", award_amount=200 )
    # form = fr.create_form(form)
    # print(form)
    # print(fr.get_all_forms())
    print("-----------")


    # account.account_num = 333333
    # account.account_type = 'Saving'
    # account.current_balance += 100
    # account.client_id = 3
    # account = ar.update_account(account)

    print("---status----")
    print(fr.get_status(101))
    print(form)


    # print("---DELETE---")
    # fr.delete_form(form.form_id)
    # print(fr.get_all_forms())
    # print(ar.get_form(form.form_id))  # ResourceNotFound - form was deleted.


if __name__ == '__main__':
    _test()
