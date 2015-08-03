from django.test import TestCase
from .models import User
from model_mommy import mommy


class UserTestMommy(TestCase):

    def test_user_creation_mommy(self):
        what = mommy.make(User)
        self.assertTrue(isinstance(what, User))
        self.assertEqual(what.__unicode__(), what.username)
