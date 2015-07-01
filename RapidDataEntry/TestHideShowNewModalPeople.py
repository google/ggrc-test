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


class TestHideShowNewModalPeople(WebDriverTestCase):

    def testHideShowNewModalPeople(self):
        self.testname="TestHideShowNewModalPeople"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        list_all = "all"
        list_items = "enabled_user, company"
        a_few_items = "company"
 
        print "TEST THAT YOU CAN SHOW OR HIDE FIELDS/ELEMENTS IN CREATE NEW OBJECT MODAL."
        
        # fill in mandatory fields only
        do.openCreateNewObjectWindowFromLhn("Person")
 
        # hide_all, show_all, then hide individual
        do.hideInNewModal(list_all, True, "person")
        do.hideInNewModal(list_all, False, "person")
        
        # hide individually
        do.hideInNewModal(list_items, True, "person")
                
        # show all again, hide a few will cause show_all to display, now reshow_all
        do.hideInNewModal(list_all, False, "person")
        do.hideInNewModal(a_few_items, True, "person")
        do.hideInNewModal(list_all, False, "person")
        
        do.populateNewObjectData(do.generateNameForTheObject("person"))
        do.saveNewObjectAndWait()


if __name__ == "__main__":
    unittest.main()