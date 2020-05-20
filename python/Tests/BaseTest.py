import unittest 
from selenium import webdriver
from Tests.pageobjects.BasePage import BasePage
from Tests.pageobjects.Header import Header


class BaseTest(unittest.TestCase):

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
        main_pageheader = BasePage(self.driver)
        BasePage.main_pagebtn(self)
        BasePage.contact_link(self)
        
    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @classmethod
    def tearDown(self):
        print("-"*20 + " Test End " + "-"*20)
        self.driver.quit()
            
            
if __name__ == '__main__':
    unittest.main(verbosity=2)