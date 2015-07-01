'''
Created on Jul 11, 2014

@author: uduong

This test script creates a new user from the LHS menu.
'''

import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestPersonCreate(WebDriverTestCase):
       
    def testPersonCreate(self):
        self.testname="TestPersonCreate"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        print "Log in as : " + do.whoAmI()
        
        number = str(do.getRandomNumber())
        aEmail = "auto_email_" + number + "@gmail.com"
        aName = do.getUniqueString("name")
        aCompany = do.getUniqueString("company")      
        do.createPersonLHN(aName, aEmail, aCompany)        
               
if __name__ == "__main__":
    unittest.main()