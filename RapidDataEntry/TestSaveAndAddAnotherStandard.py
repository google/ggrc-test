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


class TestSaveAndAddAnotherStandard(WebDriverTestCase):
    
    
    def testSaveAndAddAnotherStandard(self):
        self.testname="TestSaveAndAddAnotherStandard"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        
        object_1_name = do.generateNameForTheObject("Standard")
        do.delay(10) # count number does not appear right away, weird
        object_2_name = "Standard_" + str(do.getRandomNumber())
        
        do.ensureLHNSectionExpanded("Standard")
        count_before = do.countOfAnyObjectLHS("Standard")
        do.createObjectSaveAddAnother("Standard", object_1_name, "unchecked", True, "", False)
        do.createObjectSaveAddAnother("Standard", object_2_name, "unchecked", False, "", True)
        do.clearSearchBoxOnLHS() #clear any text so total count displays
        do.ensureLHNSectionExpanded("Standard")
        count_after = do.countOfAnyObjectLHS("Standard")
              
        do.assertEqual(count_after, count_before+2, "Count has not incremented by 1 as expected.") 
               
        print "Object 1: "
        object_1_link = do.verifyObjectIsCreatedinLHN("Standard", object_1_name)
        do.navigateToObjectAndOpenObjectEditWindow("Standard",object_1_link)
        do.deleteObject()
        
        print "Object 2: "
        object_2_link = do.verifyObjectIsCreatedinLHN("Standard", object_2_name)
        do.navigateToObjectAndOpenObjectEditWindow("Standard",object_2_link)
        do.deleteObject()        
       
        
if __name__ == "__main__":
    unittest.main()

