'''
Created on Jul 31, 2013

@author: diana.tzinov
'''



import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestControlEdit(WebDriverTestCase):
    
    
    def testControlEdit(self):
        self.testname="TestControlEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        grcobject = GRCObject()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("Control")
        object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Control",last_created_object_link)
        do.populateObjectInEditWindow( object_name , grcobject.control_elements, grcobject.control_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.control_elements, grcobject.control_values)
        do.deleteObject()
        
        
if __name__ == "__main__":
    unittest.main()
