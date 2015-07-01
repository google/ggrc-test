'''
Created on Oct 17, 2013

@author: silas@reciprocitylabs.com
'''


import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers


class TestObjectiveCreate(WebDriverTestCase):

    def testObjectiveCreate(self):
        self.testname = "TestObjectiveCreate"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("Objective")
        do.navigateToObjectAndOpenObjectEditWindow("Objective", last_created_object_link)
        do.deleteObject()


if __name__ == "__main__":
    unittest.main()
