from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import os

from tags.models import Post, Tag
from .base import FunctionalTest


class SearchTagTest(FunctionalTest):

    @unittest.skipIf(
        os.environ.get('TRAVIS'),
        'Headless displayon Travis CI cannot catch autocomplete elements.'
    )
    def test_search_tag_should_show_tags_autocompleted(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_search_tag')
        inputbox.send_keys(self.common_in_tags)
        items = self.browser.find_elements_by_class_name(
            'ui-menu-item-wrapper')

        if len(items) == 0:
            self.fail("Autocompleted item should exist at least one")
        for idx, item in enumerate(items):
            self.assertEqual(self.tag[idx].tag, item.text)

    def test_post_list_should_contain_correct_posts(self):
        for i in range(10):
            self.tag[0].post.add(self.post[i])

        url = "{0}{1}".format(
            self.live_server_url,
            self.tag[0].get_absolute_url()
        )
        self.browser.get(url)

        item_text = self.browser.find_element_by_class_name('post_list').text
        item_count = item_text.count('It is text')
        for idx in range(item_count):
            self.assertIn(self.post[i].text, item_text)
