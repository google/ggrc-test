'''
Created on Aug 10, 2013

@author: diana.tzinov
'''




import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestFacilityEdit(WebDriverTestCase):
    
    
    def testFacilityEdit(self):
        self.testname="TestFacilityEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        grcobject = GRCObject()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("Facility")
        object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Facility",last_created_object_link)
        do.populateObjectInEditWindow( object_name , grcobject.facility_elements, grcobject.facility_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.facility_elements, grcobject.facility_values)
        do.deleteObject()
        
if __name__ == "__main__":
    unittest.main()
