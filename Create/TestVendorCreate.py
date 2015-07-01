'''
Created on Dec 8, 2014

@author: uduong
'''

import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestVendorCreate(WebDriverTestCase):
     
    def testVendorCreate(self):
        self.testname="TestVendorCreate"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        last_created_object_link =do.createObject("Vendor")
        do.navigateToObjectAndOpenObjectEditWindow("Vendor",last_created_object_link)
        do.deleteObject()
       
        
if __name__ == "__main__":
    unittest.main()
