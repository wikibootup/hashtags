from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

from tags.models import Post, Tag


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.post = []
        self.tag = []
        self.common_in_tags = 'tag'
        for i in range(100):
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

    def test_search_tag_should_show_tags_autocompleted(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys(self.common_in_tags)
        items = self.browser.find_elements_by_class_name(
            'ui-menu-item-wrapper')
        for idx, item in enumerate(items):
            self.assertEqual(self.tag[idx].tag, item.text)

    def test_post_list_should_contain_correct_posts(self):
        for i in range(10):
            self.tag[0].post.add(self.post[i])
        
        url = "%s/%s/%s/" % (self.live_server_url, '/tags/', self.tag[0].tag)
        self.browser.get(url)
        items = self.browser.find_elements_by_class_name('post_list') 
        for idx, item in enumerate(items):
            self.assertEqual(self.post[i].text, item.text)
