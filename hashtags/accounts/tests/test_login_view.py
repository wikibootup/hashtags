from django.test import TestCase
from accounts.views import LoginView
from accounts.forms import LoginForm

class LoginViewTest(TestCase):

    def test_login_form_in_login_page(self):
        login_url = '/accounts/login/'
        response = self.client.get(login_url)
        self.assertIsInstance(response.context['form'], LoginForm)
