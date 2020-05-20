from selenium import webdriver
import sys
from Tests.pageobjects.utilities.Logger import Log
from Tests.pageobjects.utilities.Logger import PrintTime


class BasePage():
    """
    This Class searches for
    bugs in my main page 
    """
    def __init__(self, driver):
        self.driver = driver
        print(BasePage.__doc__)
    
    def main_pagebtn(self):
        driver = self.driver
        before_clickurl = driver.current_url
        header_elems = driver.find_elements_by_tag_name("li")
        header_elems[1].click()
        after_clickurl = driver.current_url
        self.assertEqual(before_clickurl, after_clickurl,
                         "The Main Page button Broken")
        
        function_Name = sys._getframe().f_code.co_name
        PrintTime(function_Name)
        Log(function_Name) 
        
    def contact_link(self):
        
        driver = self.driver
        assert "Andrey Bessel" in driver.title
        contacts = driver.find_element_by_link_text("Leave Contacts")
        contacts.click()
        assert "Enter your contacts" in driver.page_source
        
        function_Name = sys._getframe().f_code.co_name
        PrintTime(function_Name)
        Log(function_Name) 
        
        
        

            
        