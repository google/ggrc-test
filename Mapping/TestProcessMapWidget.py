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


class TestProcessMapWidget(WebDriverTestCase):

    def testProcessMapWidget(self):
        self.testname="TestProcessMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Process")
        do.login()
        process_name = "Process for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Process", process_name)

        for obj in grcobject.process_map_to_widget: 
            do.mapAObjectWidget(obj)


if __name__ == "__main__":
    unittest.main()
