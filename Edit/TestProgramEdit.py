'''
Created on Jul 19, 2013

@author: diana.tzinov
'''



import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestProgramEdit(WebDriverTestCase):

    
    def testProgramEdit(self):
        self.testname="TestProgramEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("Program")
        object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Program",last_created_object_link)
        do.populateObjectInEditWindow( object_name , grcobject.program_elements, grcobject.program_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.program_elements, grcobject.program_values)
        do.deleteObject()
        
        
        
if __name__ == "__main__":
    unittest.main()
