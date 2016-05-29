from django.test import LiveServerTestCase
from selenium import webdriver

from posts.models import Post, Tag
from posts.forms import SearchForm


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

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
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('It is text', body_text)
        self.assertIn('tag1', body_text)
        self.assertIn('tag2', body_text)

    def test_home_has_search_tag(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SearchForm)
