'''
Created on Sep 10, 2013

@author: diana.tzinov
'''




import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestProgramMapWidget(WebDriverTestCase):

    def testProgramMapWidget(self):
        self.testname="TestProgramMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Program")
        do.login()       
        program_name = "Program for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Program", program_name)

        for obj in grcobject.program_map_to_widget: 
            do.mapAObjectWidget(obj, "", True, ("Control", "Objective", "System"))


if __name__ == "__main__":
    unittest.main()
