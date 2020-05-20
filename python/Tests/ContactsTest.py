import unittest 
from selenium import webdriver
from Tests.pageobjects.ContactsPage import ContactsPage
from Tests.pageobjects.Header import Header


class ContactsTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        assert options.headless

        self.driver = webdriver.Chrome(options=options)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:5000/")


    def test_header(self):
        Header(self.driver)
        Header.header_elements(self)
        
    def test_mainpage(self):
        ContactsPage(self.driver)
        ContactsPage.main_pagebtn(self)
        ContactsPage.send_contacts(self)

    @classmethod
    def tearDown(self):
        print("-"*20 + " Test End " + "-"*20)
        self.driver.quit
if __name__ == '__main__':
    unittest.main()