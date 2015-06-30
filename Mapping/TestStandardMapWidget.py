'''
Created on Oct 7, 2014

@author: uduong
'''


import time
import unittest

from helpers.Elements import Elements
from helpers.GRCObject import GRCObject
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestStandardMapWidget(WebDriverTestCase):

    def testStandardMapWidget(self):
        self.testname="TestStandardMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Standard")
        do.login()
        standard_name = "Standard for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Standard", standard_name)

        for obj in grcobject.standard_map_to_widget:
            do.mapAObjectWidget(obj, standard_name, False, ("Section", "Objective", "Control"))
            # do not remove standard_name

if __name__ == "__main__":
    unittest.main()
