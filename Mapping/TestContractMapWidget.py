'''
Created on Sep 15, 2013

@author: diana.tzinov
'''



import time
import unittest

from helpers.Elements import Elements
from helpers.GRCObject import GRCObject
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestContractMapWidget(WebDriverTestCase):

    def testContractMapWidget(self):
        self.testname="TestContractMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Contract")
        do.login()
        contract_name = "Contract for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Contract", contract_name)

        for obj in grcobject.contract_map_to_widget:
            do.mapAObjectWidget(obj, "", False, ("Clause", "Objective", "Control"))
            #util.refreshPage()

if __name__ == "__main__":
    unittest.main()
