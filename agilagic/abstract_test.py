from django.test import LiveServerTestCase
from django.conf import settings
from selenium import webdriver


class SeleniumTestCase(LiveServerTestCase):
    """
    A base test case for Selenium, providing hepler methods for generating
    clients and logging in profiles.
    """
    def setUp(self):
        super(SeleniumTestCase, self).setUp()
        self.web_driver = settings.WEB_DRIVER_CLASS()

    def tearDown(self):
        self.web_driver.quit()
        super(SeleniumTestCase, self).tearDown()

    def open(self, url):
        self.web_driver.get("%s%s" % (self.live_server_url, url))