'''
Created on Jul 18, 2013

@author: diana.tzinov
'''


import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers


class TestPolicyCreate(WebDriverTestCase):
    
    
    def testPolicyCreate(self):
        self.testname="TestPolicyCreate"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        last_created_object_link =do.createObject("Policy")
        do.navigateToObjectAndOpenObjectEditWindow("Policy",last_created_object_link)
        do.deleteObject()

        
        
if __name__ == "__main__":
    unittest.main()
