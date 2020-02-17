from agilagic.abstract_test import SeleniumTestCase

from user_authentication.models import User, UserManager
import re
import time

from django.test import override_settings

from agilagic.abstract_test import SeleniumTestCase


class Tests(SeleniumTestCase):
    def setUp(self):
        super().setUp()
        data = {'email': 'vd@vd.com',
                'password': 'salamsalam',
                'name': 'name',
                'family_name': 'family_name'}
        self.user = UserManager.sign_up_user(True, data)

    def tearDown(self):
        super().tearDown()

    @staticmethod
    def help_login(selenium_test_case, username, password):
        selenium_test_case.open("/sign_in.html")
        time.sleep(1)

        web_driver = selenium_test_case.web_driver

        username_field = web_driver.find_element_by_name("email")
        password_field = web_driver.find_element_by_name("password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        submit_attempt = web_driver.find_element_by_name("submit_button")
        if submit_attempt is None:
            raise Exception

        submit_attempt.submit()
        time.sleep(1)

    @override_settings(DEBUG=True)
    def test_login_successful(self):
        self.help_login(self, username="vd@vd.com", password="salamsalam")
        self.assertTrue("Agilagic" in self.web_driver.page_source)

    @override_settings(DEBUG=True)
    def test_login_wrong_username_password(self):
        self.help_login(self, username="vd@vd.com", password="qwertyuiop[]")
        self.assertTrue("رمز عبور اشتباه است" in self.web_driver.page_source)
