'''
Created on Dec 7, 2014

@author: uduong
'''

import time
import unittest
from helpers.Elements import Elements
from helpers.GRCObject import GRCObject
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *

class TestVendorMapWidget(WebDriverTestCase):

    def testVendorMapWidget(self):
        self.testname="TestVendorMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Vendor")
        do.login()
        vendor_name = "Vendor for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Vendor", vendor_name)

        for obj in grcobject.vendor_map_to_widget: 
            do.mapAObjectWidget(obj, "")
            #util.refreshPage()

if __name__ == "__main__":
    unittest.main()