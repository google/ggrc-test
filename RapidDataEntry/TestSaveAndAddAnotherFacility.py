'''
Created on Jan 15, 2015

Description:  This class tests that you can create multiple objects via using the "Save & Add Another" button.

@author: uduong
'''

import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestSaveAndAddAnotherFacility(WebDriverTestCase):
    
    
    def testSaveAndAddAnotherFacility(self):
        self.testname="TestSaveAndAddAnotherFacility"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        
        object_1_name = do.generateNameForTheObject("Facility")
        do.delay(10) # count number does not appear right away, weird
        object_2_name = "Facility_" + str(do.getRandomNumber())
        
        do.ensureLHNSectionExpanded("Facility") # need to be expanded to see count
        count_before = do.countOfAnyObjectLHS("Facility")
        do.createObjectSaveAddAnother("Facility", object_1_name, "unchecked", True, "", False)
        do.createObjectSaveAddAnother("Facility", object_2_name, "unchecked", False, "", True)
        do.clearSearchBoxOnLHS() #clear any text so total count displays
        do.ensureLHNSectionExpanded("Facility")
        count_after = do.countOfAnyObjectLHS("Facility")
              
        do.assertEqual(count_after, count_before+2, "Count has not incremented by 1 as expected.") 
               
        print "Object 1: "
        object_1_link = do.verifyObjectIsCreatedinLHN("Facility", object_1_name)
        do.navigateToObjectAndOpenObjectEditWindow("Facility",object_1_link)
        do.deleteObject()
        
        print "Object 2: "
        object_2_link = do.verifyObjectIsCreatedinLHN("Facility", object_2_name)
        do.navigateToObjectAndOpenObjectEditWindow("Facility",object_2_link)
        do.deleteObject()        
       
        
if __name__ == "__main__":
    unittest.main()

