from django.test import TestCase

from django.contrib.auth.models import User

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class UiTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
        

    def test_login(self):
        User.objects.create_user('testuser', 'testuser@library.com', 'testpassword')
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('testpassword')
        self.selenium.find_element_by_xpath('//button[text()="Log in"]').click()

        """check that the login was successful"""
        self.selenium.find_element_by_class_name('news_article')


    def test_registration(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_name("password1")
        password_input.send_keys('testpassword')
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys('testpassword')
        self.selenium.find_element_by_xpath('//button[text()="Sign Up"]').click()

        """check that the registration was successful"""
        self.selenium.find_element_by_xpath('//button[text()="Log in"]')