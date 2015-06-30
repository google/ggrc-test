'''
Created on Jan 16, 2015

@author: ukyo duong
'''

import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestClauseEdit(WebDriverTestCase):
    
    
    def testClauseEdit(self):
        self.testname="TestClauseEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        grcobject = GRCObject()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("Clause")
        object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Clause",last_created_object_link)
        do.populateObjectInEditWindow( object_name , grcobject.clause_elements, grcobject.clause_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.clause_elements, grcobject.clause_values)
        do.deleteObject()
        
        
if __name__ == "__main__":
    unittest.main()
