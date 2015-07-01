'''
Created on Jul 14, 2014

@author: uduong
'''

import unittest

from helpers.Elements import Elements
from helpers.GRCObject import GRCObject
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *
import time

class TestCreateUpdateDeleteRegulation(WebDriverTestCase):

    def testCreateUpdateDeleteRegulation(self):
        self.testname="TestCreateUpdateDeleteRegulation"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util)
        myUtil = do.getUtils()
        do.login()
        
        last_created_object_link = do.createObject("Regulation")
        object_name = str(do.util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Regulation", last_created_object_link)
        do.populateObjectInEditWindow(object_name , grcobject.regulation_elements, grcobject.regulation_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.regulation_elements, grcobject.regulation_values)
        do.deleteObject()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()