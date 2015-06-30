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


class TestRegulationMapWidget(WebDriverTestCase):

    def testRegulationMapWidget(self):
        self.testname="TestRegulationMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Regulation")
        do.login()
        regulation_name = "Regulation for Auto Mapping from Widget" + do.getTimeId()
        last_created_object_link = do.createObject("Regulation", regulation_name)

        for obj in grcobject.regulation_map_to_widget: 
            do.mapAObjectWidget(obj, regulation_name, False, ("Objective", "Control", "Section"))
            #util.refreshPage()


if __name__ == "__main__":
    unittest.main()
