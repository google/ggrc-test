'''
Created on Dec 2, 2014

    Verify that different roles exist.

@author: uduong
'''


import time
import unittest

from helpers.Elements import Elements
from helpers.GRCObject import GRCObject
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestAllRolesPresent(WebDriverTestCase):
    
    
    def testAllRolesPresent(self):
        self.testname="TestAllRolesPresent"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
               
        do.selectMenuInTopRight("Admin Dashboard")
        do.selectMenuItemInnerNavDashBoard("Roles")
        do.verifyDifferentRolesExist() 

if __name__ == "__main__":
    unittest.main()
