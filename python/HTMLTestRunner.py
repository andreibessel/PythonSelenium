import unittest 
from HtmlTestRunner import HTMLTestRunner
from Tests.AboutPageTest import AboutTest
from Tests.BaseTest import BaseTest
from Tests.CurrencyConverterTest import CurrencyConverterTest
from Tests.ContactsTest import ContactsTest


about_test = unittest.TestLoader().loadTestsFromTestCase(AboutTest)
base_test = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
currency_test = unittest.TestLoader().loadTestsFromTestCase(CurrencyConverterTest)
contacs_test = unittest.TestLoader().loadTestsFromTestCase(ContactsTest)

suite = unittest.TestSuite([about_test, base_test, currency_test, contacs_test])
#suite = unittest.TestSuite([currency_test, contacs_test])

runner = HTMLTestRunner(output='Results')

runner.run(suite)