from selenium import webdriver
import sys
import time
import os

from Tests.pageobjects.utilities.Logger import Log
from Tests.pageobjects.utilities.Logger import PrintTime

class AboutPage():
    """
    This Class searches for
    bugs in my about page 
    """
    def __init__(self, driver):
        self.driver = driver
        print(AboutPage.__doc__)
    
    def about_btns(self):
        driver = self.driver

        assert "My Resume" in driver.page_source
        buttons = driver.find_elements_by_tag_name("button")
        self.assertEqual(len(buttons), 2,
                         "We are missing a button")
        
        function_Name = sys._getframe().f_code.co_name
        PrintTime(function_Name)
        Log(function_Name) 

    def about_btnsclick(self):
        driver = self.driver
        
        buttons = driver.find_elements_by_tag_name("button")
        for btn in buttons:
            btn.click()
            time.sleep(2)
        
        function_Name = sys._getframe().f_code.co_name
        PrintTime(function_Name)
        Log(function_Name) 
        
    def files_downloaded(self):
        dir_content = os.listdir()
        assert 'Andrey_Bessel.docx' in dir_content
        assert 'andrey_hebrew.docx' in dir_content
        folder = os.getcwd()
        filenames = ['Andrey_Bessel.docx',
             'andrey_hebrew.docx']
        try:
            for file in filenames:
                file_path = os.path.join(folder, file)
                os.remove(file_path)
        except FileNotFoundError:
            print("No files found to remove")

        
        