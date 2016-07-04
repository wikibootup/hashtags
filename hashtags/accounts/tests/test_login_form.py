from django.test import TestCase
from accounts.forms import LoginForm

class LoginFormTest(TestCase):

    def setUp(self):
        self.valid_email = 'valid@gmail.com'
        self.valid_password = 'valid_123*'

    def test_login_form_validation_for_blank_items(self):
        email_blank_form = LoginForm(
            data={'email': '', 'password': self.valid_password}
        )
        self.assertFalse(email_blank_form.is_valid())

        password_blank_form = LoginForm(
            data={'email': self.valid_email, 'password': ''}
        )
        self.assertFalse(password_blank_form.is_valid())
