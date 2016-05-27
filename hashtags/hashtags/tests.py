from django.core.urlresolvers import resolve
from django.test import TestCase

import hashtags.views


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, hashtags.views.home)
