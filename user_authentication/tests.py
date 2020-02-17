from agilagic.abstract_test import SeleniumTestCase

from user_authentication.models import User
import re
import time

from django.test import override_settings

from agilagic.abstract_test import SeleniumTestCase


class Tests(SeleniumTestCase):
    def setUp(self):
        super().setUp()
        self.super_user = User.objects.create_superuser(
            username="vd",
            first_name="vahid",
            last_name="bala",
            password="salamsalam",
            email="vahid@agilagic.com"
        )

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
        self.help_login(self, username="vd", password="salamsalam")
        self.assertTrue("Agilagic" in self.web_driver.page_source)

    @override_settings(DEBUG=True)
    def test_login_wrong_username_password(self):
        self.help_login(self, username="vd", password="qwertyuiop[]")
        self.assertTrue("رمز عبور اشتباه است" in self.web_driver.page_source)
