'''
Created on Jul 24, 2013

@author: diana.tzinov
'''


import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers


class TestSystemCreate(WebDriverTestCase):
    
    
    def testSystemCreate(self):
        self.testname="TestSystemCreate"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        last_created_object_link =do.createObject("System")
        #object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("System",last_created_object_link)
        do.deleteObject()

        
        
if __name__ == "__main__":
    unittest.main()
