from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase

import hashtags.views
from posts.forms import SearchForm


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, hashtags.views.home)

    def test_home_returns_correct_html(self):
        request = HttpRequest()
        response = hashtags.views.home(request)
        expected_html = render_to_string('home.html', {'form': SearchForm()})
        self.assertMultiLineEqual(response.content.decode(), expected_html)
