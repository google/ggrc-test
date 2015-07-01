'''
Created on Sep 21, 2013

@author: diana.tzinov
'''



import time
import unittest

from helpers.Elements import Elements
from helpers.GRCObject import GRCObject
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestOrgGroupMapLHN(WebDriverTestCase):

    
    def testOrgGroupMapLHN(self):
        self.testname="TestOrgGroupMapLHN"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "OrgGroup")
        do.login()
        system_name = "OrgGroup for Auto Mapping from LHN"  +do.getTimeId()
        last_created_object_link = do.createObject("OrgGroup", system_name)

        for obj in grcobject.org_group_map_to_lhn: 
            do.mapAObjectLHN(obj)
       
        # test unmapping
        for obj in grcobject.org_group_map_to_lhn: 
            self.assertTrue(do.unmapAObjectFromWidget(obj))

        
if __name__ == "__main__":
    unittest.main()
