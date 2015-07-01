'''
Created on Dec 7, 2014

@author: uduong
'''

import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestVendorMapLHN(WebDriverTestCase):
   
    def testVendorMapLHN(self):
        self.testname="TestVendorMapLHN"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Vendors")
        do.login()      
        
        contract_name = "Vendors for Auto Mapping from LHN"  + do.getTimeId()
        
        last_created_object_link = do.createObject("Vendor", contract_name)

        for obj in grcobject.vendor_map_to_lhn: 
            do.mapAObjectLHN(obj)
            #util.refreshPage()
       
        # test unmapping
        for obj in grcobject.vendor_map_to_lhn: 
            self.assertTrue(do.unmapAObjectFromWidget(obj))


if __name__ == "__main__":
    unittest.main()
