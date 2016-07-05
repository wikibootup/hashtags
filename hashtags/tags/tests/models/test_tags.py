from django.test import TestCase

from tags.models import Post, Tag


class TagTest(TestCase):

    def test_get_absoloute_url_tag_post_list(self):
        tag = Tag.objects.create(tag='tagName')
        hardcoded_url = "/{0}/{1}/".format('tags', tag.tag)
        absoulte_url = tag.get_absolute_url()
        self.assertEqual(absoulte_url, hardcoded_url)
