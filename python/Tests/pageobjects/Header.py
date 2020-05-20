from selenium import webdriver
import sys
from Tests.pageobjects.utilities.Logger import Log
from Tests.pageobjects.utilities.Logger import PrintTime
class Header():
    """
    This Class searches for
    bugs in my Header 
    """
    def __init__(self, driver):
        self.driver = driver
        print(Header.__doc__)
    
    def header_elements(self):
        driver = self.driver
        header_elems = driver.find_elements_by_xpath(r"//li/a")
        header_elemsconst = 6
        self.assertEqual(len(header_elems), header_elemsconst,
                         "Some elements of header are missing")
        page_linktext = ["Main Page", "About",
                         "Currency Converter", "Contacts"]        
        count = 0
        for i in header_elems:
            for y in page_linktext:
                if i.text == y:
                    count += 1
        self.assertEqual(count, len(page_linktext),
                         "Some text is missing in header")
        
        function_Name = sys._getframe().f_code.co_name
        PrintTime(function_Name)
        Log(function_Name) 