# -*- coding: utf-8 -*-

from django.test import TestCase

from posts.forms import SearchForm


class SearchTagsTest(TestCase):

    def test_form_renders_search_tags_input(self):
        form = SearchForm()
        self.assertIn('placeholder="검색"', form.as_p())

    def test_search_tags_query_out_correct_posts(self):
        """
        It assumes that the two posts are linked in 'tag1'.
        New visitor searches 'tag1', then the two posts are queried out in the
        result.
        """

        post1 = Post(text='It is text1')
        post1.save()

        post2 = Post(text='It is text2')
        post2.save()

        tag1 = Tag(tag='tag1')
        tag1.save()

        tag1.post.add(post1)
        tag1.post.add(post2)

        connect('/')
        result = search('tag1')
        self.assertTrue(post1.text in result)
        self.assertTrue(post2.text in result)
