from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base import FunctionalTest


class LoginTest(FunctionalTest):

    def test_login_link_redirect_login_page(self):
        login_url = '/accounts/login/'

        self.browser.get(self.live_server_url)
        login_link = self.browser.find_element_by_class_name('loginLink')
        login_link.click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "testLogin"))
        )

        current_url = self.browser.current_url
        self.assertTrue(current_url.endswith(login_url))
