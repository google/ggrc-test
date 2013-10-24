'''
Created on Oct 24, 2013

@author: silas@reciprocitylabs.com
'''


import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers


class BaseTestCreate(WebDriverTestCase):
    
    def _create_test(self, object_type):
        self.testname = "test{0}Create".format(object_type)
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject(object_type)
        do.navigateToObjectAndOpenObjectEditWindow(object_type, last_created_object_link)
        do.deleteObject()


if __name__ == "__main__":
    unittest.main()
