# -*- coding: utf-8 -*-

from django.test import TestCase

from posts.forms import SearchForm
from posts.models import Post, Tag


class SearchTagsTest(TestCase):

    def setUp(self):
        self.post = []
        self.tag = []
        for i in range(10):
            self.post.append(Post(text='It is text%s' % (i+1)))
            self.post[i].save()
            self.tag.append(Tag(tag='tag%s' % (i+1)))
            self.tag[i].save()

    def test_form_renders_search_tag_input(self):
        form = SearchForm()
        self.assertIn('placeholder="검색"', form.as_p())

    def test_search_tag_query_out_correct_posts(self):
        """
        It assumes that the two posts are linked in 'tag1'.
        New visitor searches 'tag1', then the two posts are queried out in the
        result.
        """

        self.tag[0].post.add(self.post[0])
        self.tag[0].post.add(self.post[1])

        response = self.client.get('/', data={'search_tag': self.tag[0].tag})
        self.assertContains(response, self.post[0].text)
        self.assertContains(response, self.post[1].text)
