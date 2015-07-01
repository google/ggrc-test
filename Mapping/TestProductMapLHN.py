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


class TestProductMapLHN(WebDriverTestCase):

    
    def testProductMapLHN(self):
        self.testname="TestProductMapLHN"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Product")
        do.login()
        system_name = "Product for Auto Mapping from LHN"  +do.getTimeId()
        last_created_object_link = do.createObject("Product", system_name)

        for obj in grcobject.product_map_to_lhn: 
            do.mapAObjectLHN(obj)
       
        # test unmapping
        for obj in grcobject.product_map_to_lhn: 
            self.assertTrue(do.unmapAObjectFromWidget(obj))
        
if __name__ == "__main__":
    unittest.main()
