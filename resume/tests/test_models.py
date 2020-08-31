from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError
from django.test import TestCase
from resume.models import Resume, Education


class ItemModelTest(TestCase):

    def test_default_text(self):
        resume = Resume()
        self.assertEqual(resume.display_name, '')

