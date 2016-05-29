from django.test import TestCase

from posts.models import Post


class PostTest(TestCase):
    
    def test_post_contains_correct_text_and_tags(self):
        post = Post.create_object(text='It is text', tags=('tag1', 'tag2'))

        self.assertEqual('It is text', post.text)
        self.assertContains('tag1', post.tags)
        self.assertContains('tag2', post.tags)
