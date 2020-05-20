import unittest
from Tests.AboutPageTest import AboutTest
from Tests.BaseTest import BaseTest
from Tests.CurrencyConverterTest import CurrencyConverterTest
from Tests.ContactsTest import ContactsTest


about_test = unittest.TestLoader().loadTestsFromTestCase(AboutTest)
base_test = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
currency_test = unittest.TestLoader().loadTestsFromTestCase(CurrencyConverterTest)
contacs_test = unittest.TestLoader().loadTestsFromTestCase(ContactsTest)

suite = unittest.TestSuite([about_test, base_test, currency_test, contacs_test])



unittest.TextTestRunner(verbosity=2).run(suite)