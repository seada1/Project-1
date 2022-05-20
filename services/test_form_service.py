# import unittest
# from unittest.mock import MagicMock
#
# from models.form import Form
# from repositories.form_repo_impl import FormRepoImpl
# from services.form_service import FormService
#
#
# class TestFormService(unittest.TestCase):
#     fr = FormRepoImpl()
#     fs = FormService(fr)
#
#    # def test_get_form_above_price(self):
#         # self.fs.get_all_forms = MagicMock(return_value=[
#         #     Form(movie_id=1, title="Thor", price=3, genre=1),
#         #     Form(movie_id=2, title="Captain Marvel", price=4, genre=2),
#         #     Form(movie_id=3, title="The Avengers", price=5, genre=3)
#         # ])
#         #
#         # refined_movies = self.fs.get_form_above_price(4)
#         # print(refined_movies)
#         #
#         # self.assertListEqual(refined_movies, [
#         #     Movie(movie_id=2, title="Captain Marvel", price=4, genre=2),
#         #     Movie(movie_id=3, title="The Avengers", price=5, genre=3)
#         # ])
#
#
# if __name__ == '__main__':
#     unittest.main()
