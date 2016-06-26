from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from unittest import skip

from tags.models import Post, Tag
from tags.forms import SearchForm


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.post = []
        self.tag = []
        self.common_in_tags = 'tag'
        for i in range(10):
            self.post.append(Post(text='It is text%s' % (i+1)))
            self.post[i].save()
            self.tag.append(Tag(tag='tag%s' % (i+1)))
            self.tag[i].save()

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
        self.tag[0].post.add(self.post[0])

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys(self.tag[0].tag)
        inputbox.send_keys(Keys.ENTER)

        self.assertEqual(
            self.live_server_url + '/?search_tag=' + self.tag[0].tag,
            self.browser.current_url
        )

    def test_search_tag_query_results_correct_posts(self):
        """
        It assumes that the two posts are linked in 'self.tag[0]'.
        New visitor searches 'self.tag[0]', then the two posts are queried out in the
        result.
        """

        self.tag[0].post.add(self.post[0])
        self.tag[0].post.add(self.post[1])

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys(self.tag[0].tag)
        inputbox.send_keys(Keys.ENTER)

        list_posts = self.browser.find_element_by_id('id_list_posts')
        self.assertIn(self.post[0].text, list_posts.text)
        self.assertIn(self.post[1].text, list_posts.text)
        self.assertNotIn(self.post[0].text, self.post[2].text)

    def test_search_tag_query_count_correct_numbers(self):
        """
        It assumes that the two posts are linked in 'self.tag[0]'.
        New visitor searches 'self.tag[0]', then the two posts are queried out in the
        result.
        """

        self.tag[0].post.add(self.post[0])
        self.tag[0].post.add(self.post[1])

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys(self.tag[0].tag)
        inputbox.send_keys(Keys.ENTER)

        list_posts = self.browser.find_element_by_id('id_list_posts')
        p_posts = list_posts.find_elements_by_tag_name('p')
        self.assertEqual(len(p_posts), 2)

    def test_search_tag_should_show_tags_autocompleted(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys(self.common_in_tags)
        items = self.browser.find_elements_by_class_name(
            'ui-menu-item-wrapper')
        for idx, item in enumerate(items):
            self.assertEqual(self.tag[idx].tag, item.text)
