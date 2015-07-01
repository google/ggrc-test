'''
Created on Jun 17, 2013

@author: diana.tzinov
'''
import unittest
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers


class TestLogin(WebDriverTestCase):
    
    
    def testLogin(self):
        self.testname="TestLogin"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        self.assertTrue(util.isElementPresent(element.dashboard_title), "no dashboard page found")
        
if __name__ == "__main__":
    unittest.main()
