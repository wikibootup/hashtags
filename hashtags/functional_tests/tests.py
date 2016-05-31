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

    def test_home_has_search_tag(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SearchForm)

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

        self.assertEqual(
            self.live_server_url + '/?search_tag=' + tag1.tag,
            self.browser.current_url
        )

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

        post3 = Post(text='It is text3')
        post3.save()

        tag1 = Tag(tag='tag1')
        tag1.save()

        tag1.post.add(post1)
        tag1.post.add(post2)

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys('tag1')
        inputbox.send_keys(Keys.ENTER)

        list_posts = self.browser.find_element_by_id('id_list_posts')
        self.assertIn(post1.text, list_posts.text)
        self.assertIn(post1.text, list_posts.text)
        self.assertNotIn(post1.text, post3.text)

    def test_search_tag_query_count_correct_numbers(self):
        """
        It assumes that the two posts are linked in 'tag1'.
        New visitor searches 'tag1', then the two posts are queried out in the
        result.
        """

        post1 = Post(text='It is text1')
        post1.save()

        post2 = Post(text='It is text2')
        post2.save()

        post3 = Post(text='It is text3')
        post3.save()

        tag1 = Tag(tag='tag1')
        tag1.save()

        tag1.post.add(post1)
        tag1.post.add(post2)

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys('tag1')
        inputbox.send_keys(Keys.ENTER)

        list_posts = self.browser.find_element_by_id('id_list_posts')
        p_posts = list_posts.find_elements_by_tag_name('p')
        self.assertEqual(len(p_posts), 2)
