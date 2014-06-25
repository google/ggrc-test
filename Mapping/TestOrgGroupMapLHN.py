'''
Created on Sep 21, 2013

@author: diana.tzinov
'''



import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers
from helperRecip.GRCObject import GRCObject


class TestOrgGroupMapLHN(WebDriverTestCase):

    
    def testOrgGroupMapLHN(self):
        self.testname="TestOrgGroupMapLHN"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers(self)
        do.setUtils(util, "OrgGroup")
        do.login()
        
        # Uncomment these when run this test by itself in standalone or troubleshoot session   
        # Objects must exist before mapping can be done 
        do.createObject("Program")
        do.createObject("Regulation")
        do.createObject("Contract")
        do.createObject("Policy")
        do.createObject("Control")
        do.createObject("Objective")
        do.createObject("System")
        do.createObject("Process")
        do.createObject("Data")             
        do.createObject("Product")
        do.createObject("Project")           
        do.createObject("Facility")
        do.createObject("Market")
        
        
        system_name = "OrgGroup for Auto Mapping from LHN"  +do.getTimeId()
        last_created_object_link = do.createObject("OrgGroup", system_name)
        #object_name = str(util.getTextFromXpathString(last_created_object_link)).strip() 
        #do.navigateToObjectWithSearch(system_name, "OrgGroup")
        for obj in grcobject.org_group_map_to_lhn: 
            do.mapAObjectLHN(obj)
            #util.refreshPage()
       

        
if __name__ == "__main__":
    unittest.main()
