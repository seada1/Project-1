from exceptions.resource_unavailable import ResourceUnavailable
from models.form import Form
from repositories.form_repo import FormRepo
from repositories.form_repo_impl import FormRepoImpl


class FormService:

    # Dependency Injection - having dependencies Not managed by a Class and instead provided to them at some point.
    def __init__(self, form_repo: FormRepo):
        self.form_repo = form_repo

    def create_form(self, form):
        return self.form_repo.create_form(form)

    def get_form(self, form_id):
        return self.form_repo.get_form(form_id)

    def get_all_forms(self):
        return self.form_repo.get_all_forms()

    def get_status(self, form_id):
        return self.form_repo.get_status(form_id)

    def update_form(self, change):
        return self.form_repo.update_form(change)

    def delete_form(self, form_id):
        return self.form_repo.delete_form(form_id)


def _test():

     fr: FormRepo = FormRepoImpl()
     fs: FormService = FormService(fr)

     form = fs.get_form(101)
     print(form)


if __name__ == '__main__':
    _test()