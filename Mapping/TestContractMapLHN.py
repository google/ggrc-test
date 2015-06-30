'''
Created on Sep 22, 2013

@author: ukyo.duong
'''

import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestContractMapLHN(WebDriverTestCase):
   
    def testContractMapLHN(self):
        self.testname="TestContractMapLHN"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "Contract")
        do.login()      
        
        contract_name = "Contract for Auto Mapping from LHN"  + do.getTimeId()
        
        last_created_object_link = do.createObject("Contract", contract_name)

        for obj in grcobject.contract_map_to_lhn: 
            do.mapAObjectLHN(obj)
            #util.refreshPage()
       
        # test unmapping
        for obj in grcobject.contract_map_to_lhn: 
            self.assertTrue(do.unmapAObjectFromWidget(obj))


if __name__ == "__main__":
    unittest.main()
