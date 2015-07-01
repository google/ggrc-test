'''
Created on Sep 21, 2013

@author: diana.tzinov
'''




import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestObjectiveEdit(WebDriverTestCase):
    
    
    def testObjectiveEdit(self):
        self.testname="TestObjectiveEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        grcobject = GRCObject()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("Objective")
        object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Objective",last_created_object_link)
        do.populateObjectInEditWindow( object_name , grcobject.objective_elements, grcobject.objective_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.objective_elements, grcobject.objective_values)
        do.deleteObject()
        
if __name__ == "__main__":
    unittest.main()
