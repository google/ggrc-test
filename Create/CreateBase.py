'''
Created on Jul 18, 2013

@author: diana.tzinov
'''


import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers


class BaseTestCreate(WebDriverTestCase):
    def __init__(self, object_type):
        self.object_type = object_type
        self.testname = "test{0}Create".format(object_type)
    
    def _testCreate(self, object_type):
        pass

    def testPolicyCreate(self):
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject(self.object_type)
        do.navigateToObjectAndOpenObjectEditWindow(self.object_type,last_created_object_link)
        do.deleteObject()

class TestPolicyCreate(BaseTestCreate):
    def testPolicyCreate(self):
        self._testCreate("Policy")

        
        
if __name__ == "__main__":
    unittest.main()
