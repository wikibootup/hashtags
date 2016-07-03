from django.test import LiveServerTestCase
from selenium import webdriver

from tags.models import Tag, Post


class FunctionalTest(LiveServerTestCase):

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
