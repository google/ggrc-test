'''
Created on Sep 22, 2013

@author: diana.tzinov
'''



import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestProductMapWidget(WebDriverTestCase):

    def testProductMapWidget(self):
        self.testname="TestProductMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Product")
        do.login()
        product_name = "Product for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Product", product_name)

        for obj in grcobject.product_map_to_widget: 
            do.mapAObjectWidget(obj)

if __name__ == "__main__":
    unittest.main()
