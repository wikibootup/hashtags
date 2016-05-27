from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

import hashtags.views


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, hashtags.views.home)

    def test_home_returns_correct_html(self):
        request = HttpRequest()
        response = hashtags.views.home(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>hashtags</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
