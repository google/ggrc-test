'''
Created on Aug 21, 2013

@author: diana.tzinov
'''

import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestOrgGroupEdit(WebDriverTestCase):
    
    
    def testOrgGroupEdit(self):
        self.testname="TestOrgGroupEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        grcobject = GRCObject()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("OrgGroup")
        object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("OrgGroup",last_created_object_link)
        do.populateObjectInEditWindow( object_name , grcobject.org_group_elements, grcobject.org_group_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.org_group_elements, grcobject.org_group_values)
        do.deleteObject()
        
        
if __name__ == "__main__":
    unittest.main()
