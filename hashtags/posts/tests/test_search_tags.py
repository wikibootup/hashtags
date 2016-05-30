# -*- coding: utf-8 -*-

from django.test import TestCase

from posts.forms import SearchForm


class SearchTagsTest(TestCase):

    def test_form_renders_search_tags_input(self):
        form = SearchForm()
        self.assertIn('placeholder="검색"', form.as_p())
