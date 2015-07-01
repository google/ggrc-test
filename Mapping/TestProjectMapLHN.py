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


class TestProjectMapLHN(WebDriverTestCase):

    
    def testProjectMapLHN(self):
        self.testname="TestProjectMapLHN"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Project")
        do.login()
        system_name = "Project for Auto Mapping from LHN"  +do.getTimeId()
        last_created_object_link = do.createObject("Project", system_name)

        for obj in grcobject.project_map_to_lhn: 
            do.mapAObjectLHN(obj)
       
        # test unmapping
        for obj in grcobject.project_map_to_lhn: 
            self.assertTrue(do.unmapAObjectFromWidget(obj))
        
if __name__ == "__main__":
    unittest.main()
