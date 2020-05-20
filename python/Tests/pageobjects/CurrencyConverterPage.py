from selenium import webdriver
import sys
from Tests.pageobjects.utilities.Logger import Log
from Tests.pageobjects.utilities.Logger import PrintTime


class CurrencyConverterPage():
    """
    This Class searches for
    bugs in my Currency Converter page 
    """
    def __init__(self, driver):
        self.driver = driver
        print(CurrencyConverterPage.__doc__)
    
    def main_pagebtn(self):
        driver = self.driver
        
        before_clickurl = driver.current_url
        currency_btn = driver.find_element_by_xpath(r"//li[4]")
        currency_btn.click()
        after_clickurl = driver.current_url
        self.assertEqual(before_clickurl, after_clickurl,
                         "The Main Page button Broken")
        
        function_Name = sys._getframe().f_code.co_name
        PrintTime(function_Name)
        Log(function_Name) 
        

        
        

            
        