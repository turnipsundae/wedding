import unittest

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.utils.translation import activate

from datetime import date
from django.utils import formats

from selenium import webdriver


class LocalizationTestCase(unittest.TestCase):
    def setUp(self):
        # Every test needs a client. We use django's built in because
        # I can't get activate to work in Selenium.
        self.client = Client()

    def test_english_redirect(self):
        # Issue a GET request with default language, follow redirects for language.
        response = self.client.get('/wedding/', follow=True)

        # Check that the response is 200.
        self.assertEqual(response.status_code, 200)
        
    def test_chinese_redirect(self):
        # Issue a GET request with chinese.
        response = self.client.get('/wedding/', HTTP_ACCEPT_LANGUAGE='zh', follow=True)        

        # Check that wedding date is in correct format
        wedding_date = date(2018,1,28).strftime('%Y年%-m月%-d日')
        wedding_date_bytes = wedding_date.encode('utf-8')
        self.assertEqual(wedding_date_bytes in response.content, True)

    def test_language_change(self):
        # Issue a POST request to change to english
        response = self.client.post('/i18n/setlang/')

        # Issue a POST request to change to chinese
