from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from unittest import skip

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

    @skip("need to connect correct url, view")
    def test_search_tag_query_results_correct_url(self):
        post1 = Post(text='It is text1')
        post1.save()

        tag1 = Tag(tag='tag1')
        tag1.save()

        tag1.post.add(post1)

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys('tag1')
        inputbox.send_keys(Keys.ENTER)

        self.assertEqual('/tag1', self.browser.current_url)

    @skip("need to add correct tag, id in template")
    def test_search_tag_query_results_correct_posts(self):
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

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys('tag1')
        inputbox.send_keys(Keys.ENTER)

        list_posts = self.browser.find_element_by_id('id_list_posts')
        posts = tags.find_elements_by_tag_name('p')

        self.assertTrue(any(post1.text in posts[0].text))
        self.assertTrue(any(post2.text in posts[1].text))
