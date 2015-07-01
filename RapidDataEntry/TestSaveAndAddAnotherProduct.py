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


class TestSaveAndAddAnotherProduct(WebDriverTestCase):
    
    
    def testSaveAndAddAnotherProduct(self):
        self.testname="TestSaveAndAddAnotherProduct"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        
        object_1_name = do.generateNameForTheObject("Product")
        do.delay(10) # count number does not appear right away, weird
        object_2_name = "Product_" + str(do.getRandomNumber())
        
        do.ensureLHNSectionExpanded("Product")
        count_before = do.countOfAnyObjectLHS("Product")
        do.createObjectSaveAddAnother("Product", object_1_name, "unchecked", True, "", False)
        do.createObjectSaveAddAnother("Product", object_2_name, "unchecked", False, "", True)
        do.clearSearchBoxOnLHS() #clear any text so total count displays
        do.ensureLHNSectionExpanded("Product")
        count_after = do.countOfAnyObjectLHS("Product")
              
        do.assertEqual(count_after, count_before+2, "Count has not incremented by 1 as expected.") 
               
        print "Object 1: "
        object_1_link = do.verifyObjectIsCreatedinLHN("Product", object_1_name)
        do.navigateToObjectAndOpenObjectEditWindow("Product",object_1_link)
        do.deleteObject()
        
        print "Object 2: "
        object_2_link = do.verifyObjectIsCreatedinLHN("Product", object_2_name)
        do.navigateToObjectAndOpenObjectEditWindow("Product",object_2_link)
        do.deleteObject()        
       
        
if __name__ == "__main__":
    unittest.main()

