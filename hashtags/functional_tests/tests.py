from django.test import LiveServerTestCase
from selenium import webdriver

from post.models import Post, Tag


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
        post = Post.create_object(post='It is text', tags=('tag1', 'tag2',))

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_elements_by_tag_name('body').text
        self.assertIn('It is text', page_text)
        self.assertIn('tag1', page_text)
        self.assertIn('tag2', page_text)
