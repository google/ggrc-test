'''
Created on Jul 29, 2014

@author: uduong

This class will create one instance of each object type.
'''

import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestCreateOneObjectOfEachType(WebDriverTestCase):
      
    def testCreateOneObjectOfEachType(self):
              
        self.testname="TestCreateOneObjectOfEachType"
        self.setup()            
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
            
        object_list = ["Contract","Control","DataAsset","Facility","Market","Objective","OrgGroup","Policy","Process","Product","Program",
                       "Project","Regulation","System","Standard","Clause"]
            
        for obj in object_list:
            do.createObject(obj)

             
if __name__ == "__main__":
    unittest.main()
