from django.test import TestCase
from library.models import Book, Loan, Publisher, Language, Author
import datetime
from django.contrib.auth.models import User

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

import time


class LoanTests(TestCase):
    def setUp(self):
        publisher = Publisher.objects.create(name="testpublisher")
        lang = Language.objects.create(language="Finnish")
        author = Author.objects.create(first_name="Jo", last_name="kke")
        book = Book.objects.create(
            title="testbook",
            publisher=publisher,
            publication_date="2020-10-10",
            language=lang
        )
        book.authors.add(author)

        self.user = User.objects.create_user(
            username='john', email='john@example.com', password='secret')

    def test_can_create_loan(self):
        book = Book.objects.get(title="testbook")
        user = self.user
        start = datetime.date.today()
        end = start + datetime.timedelta(days=14)

        loan = Loan.objects.create(
            borrowed_book = book,
            borrower = user,
            start_date = start,
            returning_date = end
        )

        self.assertEqual(loan.borrowed_book.title, 'testbook')
        self.assertEqual(loan.borrower.username, 'john')
        self.assertEqual(loan.start_date, start)
        self.assertEqual(loan.returning_date, end)


class UiTests(StaticLiveServerTestCase):
    fixtures = ['library_test_data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


    def test_book_loan(self):
        User.objects.create_user('testuser', 'testuser@library.com', 'testpassword')
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('testpassword')
        self.selenium.find_element_by_xpath('//button[text()="Log in"]').click()
        WebDriverWait(self.selenium, 10).until(
            lambda driver: driver.find_element_by_tag_name('body'))
        self.selenium.get('%s%s' % (self.live_server_url, '/library/books/16'))
        loan_button = self.selenium.find_element_by_class_name('loan_btn')
        loan_button.click()
        self.selenium.find_element_by_id("on_loan_text")
    