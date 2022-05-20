from abc import ABC, abstractmethod


class FormRepo(ABC):

    @abstractmethod
    def create_form(self, form):
        pass

    @abstractmethod
    def get_form(self, form_id):
        pass

    @abstractmethod
    def get_all_forms(self):
        pass

    @abstractmethod
    def get_status(self, form_id):
        pass

    @abstractmethod
    def update_form(self, change):
        pass

    @abstractmethod
    def delete_form(self, form_id):
        pass