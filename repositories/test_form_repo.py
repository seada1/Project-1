import unittest

from models.form import Form
from repositories.form_repo_impl import FormRepoImpl

fr = FormRepoImpl()


class TestFormRepo(unittest.TestCase):

    added_form = Form()

    def test_get_form_success(self):
        form = fr.get_form(111)
        self.assertEqual(form, Form(form_id=111, empl_id=221,
                                    location="location 3", description="description 3",
                                    cost=500, attachment="", event_id=4,
                                    grade_id=3, status="not awarded", award_amount=200))

    def test_create_form_success(self):
        TestFormRepo.added_form = fr.create_form(self.added_form)

        self.assertEqual(self.added_form, Form(form_id=self.added_form.form_id, empl_id=0,
                                    location="", description="",
                                    cost=0, attachment="", event_id=0,
                                    grade_id=0, status="", award_amount=0))

        self.assertIsNotNone(fr.get_form(self.added_form.form_id))
        print(self.added_form)

    # setUp and tearDown will execute before or after each and every test.
    # setUpClass and tearDownClass will execute Once before or after all tests.
    @classmethod
    def tearDownClass(cls):
        if cls.added_form.form_id:
            fr.delete_form(cls.added_form.form_id)


if __name__ == '__main__':
    unittest.main()
