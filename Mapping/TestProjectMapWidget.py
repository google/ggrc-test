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


class TestProjectMapWidget(WebDriverTestCase):

    def testProjectMapWidget(self):
        self.testname="TestProjectMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Project")
        do.login()
        project_name = "Project for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Project",project_name)

        for obj in grcobject.project_map_to_widget: 
            do.mapAObjectWidget(obj)
            #util.refreshPage()


if __name__ == "__main__":
    unittest.main()
