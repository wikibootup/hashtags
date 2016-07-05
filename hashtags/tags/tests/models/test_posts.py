from django.test import TestCase

from tags.models import Post, Tag


class PostTest(TestCase):

    def test_post_contains_correct_text_and_tags(self):
        post = Post(text='It is text')
        post.save()
        tag1 = Tag(tag='tag1')
        tag1.save()
        tag2 = Tag(tag='tag2')
        tag2.save()
        
        tag1.post.add(post)
        tag2.post.add(post)

        self.assertEqual('It is text', post.text)
        self.assertTrue(post.tag_set.all().get(tag='tag1'))
        self.assertTrue(post.tag_set.all().get(tag='tag2'))
