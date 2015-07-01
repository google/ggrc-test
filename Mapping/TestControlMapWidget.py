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


class TestControlMapWidget(WebDriverTestCase):

    def testControlMapWidget(self):
        self.testname="TestControlMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Control")
        do.login()
        control_name = "Control for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Control", control_name)

        for obj in grcobject.control_map_to_widget: 
            do.mapAObjectWidget(obj)
            #util.refreshPage()


if __name__ == "__main__":
    unittest.main()
