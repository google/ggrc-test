'''
Created on Jul 17, 2013

@author: diana.tzinov
'''


import time
import unittest
from helpers.GRCObject import GRCObject
from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *

class TestCreateUpdateDeleteProgram(WebDriverTestCase):
    
    
    def testCreateUpdateDeleteProgram(self):
        self.testname="TestCreateUpdateDeleteProgram"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        
        grcobject = GRCObject()
        last_created_object_link = do.createObject("Program")
        object_name = str(do.util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Program", last_created_object_link)
        do.populateObjectInEditWindow(object_name , grcobject.program_elements, grcobject.program_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.program_elements, grcobject.program_values)
        do.deleteObject()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()