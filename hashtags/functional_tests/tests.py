from django.test import LiveServerTestCase
from selenium import webdriver

from posts.models import Post, Tag


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_find_the_correct_title(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Hashtags', self.browser.title)

    def test_post_contains_correct_tags_and_text(self):
        """
        It assumes that the one post is shown to a new visitor. the visitor can
        see the post which contains text and tags.
        """
        post = Post(text='It is text')
        post.save()
        tag1 = Tag(tag='tag1')
        tag1.save()
        tag2 = Tag(tag='tag2')
        tag2.save()

        tag1.post.add(post)
        tag2.post.add(post)

        self.browser.get(self.live_server_url)
        post_table = self.browser.find_elements_by_class_name('post_table')
        self.assertIn('It is text', post_table)
        self.assertIn('tag1', post_table)
        self.assertIn('tag2', post_table)
