from selenium import webdriver
from datetime import datetime
import sys
from Tests.pageobjects.utilities.Logger import Log
from Tests.pageobjects.utilities.Logger import PrintTime


class ContactsPage():
    """
    This Class searches for
    bugs in my Contacts Page 
    """
    def __init__(self, driver):
        self.driver = driver
        print(ContactsPage.__doc__)
    
    
    def main_pagebtn(self):
        driver = self.driver
        
        before_clickurl = r"http://localhost:5000/contacts"
        currency_btn = driver.find_element_by_xpath(r"//li[5]")
        currency_btn.click()
        after_clickurl = driver.current_url
        self.assertEqual(before_clickurl, after_clickurl,
                         "The Main Page button Broken")
        
        function_Name = sys._getframe().f_code.co_name
        PrintTime(function_Name)
        Log(function_Name) 
        
        
    def send_contacts(self):
        driver = self.driver
        
        inputs = driver.find_elements_by_xpath("//input[@type='text']")
        name = inputs[0]
        email = inputs[1]

        submit_btn = driver.find_element_by_xpath("//input[@type='submit']")


        name.clear()
        name.send_keys("Test")

        email.clear()
        email.send_keys("Test@test.com")


        submit_btn.click()

        
        
        

            
        