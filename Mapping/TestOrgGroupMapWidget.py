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


class TestOrgGroupMapWidget(WebDriverTestCase):

    def testOrgGroupMapWidget(self):
        self.testname="TestOrgGroupMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "OrgGroup")
        do.login()
        org_group_name = "OrgGroup for Auto Mapping from Widget"  +do.getTimeId()
        last_created_object_link = do.createObject("OrgGroup",org_group_name)

        for obj in grcobject.org_group_map_to_widget: 
            do.mapAObjectWidget(obj)
            #util.refreshPage()


if __name__ == "__main__":
    unittest.main()
