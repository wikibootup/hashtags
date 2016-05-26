from selenium import webdriver
from django.test import TestCase


class NewVisitorTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_find_the_correct_title(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Hashtags', self.browser.title)
