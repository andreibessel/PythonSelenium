import unittest 
from selenium import webdriver
from Tests.pageobjects.AboutPage import AboutPage
from Tests.pageobjects.Header import Header

class AboutTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        assert options.headless

        self.driver = webdriver.Chrome(options=options)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:5000/about")
        
    def test_header(self):
        Header(self.driver)
        Header.header_elements(self)
        
    def test_mainpage(self):
        AboutPage(self.driver)
        AboutPage.about_btns(self)
        AboutPage.about_btnsclick(self)
        AboutPage.files_downloaded(self)
        

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass
        
    @classmethod
    def tearDown(self):
        print("-"*20 + " Test End " + "-"*20)
        self.driver.quit()
          
            
     
if __name__ == '__main__':
    unittest.main(verbosity=2)
    