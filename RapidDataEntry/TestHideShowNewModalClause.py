'''
Created on Jan 12, 2015

@author: uduong
'''
import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestHideShowNewModalClause(WebDriverTestCase):

    def testHideShowNewModalClause(self):
        self.testname="TestHideShowNewModalClause"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        list_all = "all"
        list_items = "text_of_clause, note, owner, contact, reference_url, code"
        a_few_items = "reference_url, code"
 
        print "TEST THAT YOU CAN SHOW OR HIDE FIELDS/ELEMENTS IN CREATE NEW OBJECT MODAL."
        
        # fill in mandatory fields only
        do.openCreateNewObjectWindowFromLhn("Clause")
 
        # hide_all, show_all, then hide individual
        do.hideInNewModal(list_all, True, "clause")
        do.hideInNewModal(list_all, False, "clause")
        
        # hide individually
        do.hideInNewModal(list_items, True)
                
        # show all again, hide a few will cause show_all to display, now reshow_all
        do.hideInNewModal(list_all, False, "clause")
        do.hideInNewModal(a_few_items, True, "clause")
        do.hideInNewModal(list_all, False, "clause")
        
        do.populateNewObjectData(do.generateNameForTheObject("clause"))
        do.saveNewObjectAndWait()
        do.clickInfoPageEditLink()
               
        # now start testing hide/show after clicking on the Edit link
        do.hideInNewModal(list_all, True, "clause")
        do.hideInNewModal(list_all, False, "clause")         
        do.hideInNewModal(a_few_items, True, "clause")
        do.hideInNewModal(list_all, False, "clause") 


if __name__ == "__main__":
    unittest.main()