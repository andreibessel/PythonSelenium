import unittest 
from selenium import webdriver
from Tests.pageobjects.CurrencyConverterPage import CurrencyConverterPage
from Tests.pageobjects.Header import Header

class CurrencyConverterTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        assert options.headless

        self.driver = webdriver.Chrome(options=options)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://127.0.0.1:5000/currency")
        
    def test_header(self):
        Header(self.driver)
        Header.header_elements(self)
        
    def test_mainpage(self):
        CurrencyConverterPage(self.driver)
        CurrencyConverterPage.main_pagebtn(self)
             
        
    @classmethod
    def tearDown(self):
        print("-"*20 + " Test End " + "-"*20)
        self.driver.quit()
          
            
     
if __name__ == '__main__':
    unittest.main(verbosity=2)
    