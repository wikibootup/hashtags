from django.test import TestCase

from posts.models import Post, Tag


class TagTest(TestCase):

    def test_tag_itself_return_tag_name(self):
        tag1 = Tag(tag='tag1')
        tag1.save()
        tag2 = Tag(tag='tag2')
        tag2.save()

        self.assertEqual('tag1', tag1)
        self.assertEqual('tag2', tag2)
