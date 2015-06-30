'''
Created on Sep 15, 2013

@author: diana.tzinov
'''



import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestPolicyMapWidget(WebDriverTestCase):

    def testPolicyMapWidget(self):
        self.testname="TestPolicyMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Policy")
        do.login()       
        policy_name = "Policy for Auto Mapping from Widget"  +do.getTimeId()
        last_created_object_link = do.createObject("Policy", policy_name)

        for obj in grcobject.policy_map_to_widget: 
            do.mapAObjectWidget(obj, policy_name, False, ("Section", "Objective", "Control"))
            #util.refreshPage()


if __name__ == "__main__":
    unittest.main()
