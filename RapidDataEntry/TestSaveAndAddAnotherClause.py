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


class TestSaveAndAddAnotherClause(WebDriverTestCase):
    
    
    def testSaveAndAddAnotherClause(self):
        self.testname="TestSaveAndAddAnotherClause"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        
        object_1_name = do.generateNameForTheObject("Clause")
        do.delay(10) # count number does not appear right away, weird
        object_2_name = "Clause_" + str(do.getRandomNumber())
        
        do.ensureLHNSectionExpanded("Clause") # need to be expanded to see count
        count_before = do.countOfAnyObjectLHS("Clause") 
        do.createObjectSaveAddAnother("Clause", object_1_name, "unchecked", True, "", False)
        do.createObjectSaveAddAnother("Clause", object_2_name, "unchecked", False, "", True)
        do.clearSearchBoxOnLHS() #clear any text so total count displays
        do.expandObjectGroup("Clause") # need to be expanded to see count
        do.delay(15)
        count_after = do.countOfAnyObjectLHS("Clause")
        
        do.assertEqual(count_after, count_before+int(2), "Count has not incremented by 2 as expected.") 
               
        print "Object 1: "
        object_1_link = do.verifyObjectIsCreatedinLHN("Clause", object_1_name)
        do.navigateToObjectAndOpenObjectEditWindow("Clause",object_1_link)
        do.deleteObject()
        
        print "Object 2: "
        object_2_link = do.verifyObjectIsCreatedinLHN("Clause", object_2_name)
        do.navigateToObjectAndOpenObjectEditWindow("Clause",object_2_link)
        do.deleteObject()        
       
        
if __name__ == "__main__":
    unittest.main()

