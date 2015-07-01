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


class TestHideShowNewModalMarket(WebDriverTestCase):

    def testHideShowNewModalMarket(self):
        self.testname="TestHideShowNewModalMarket"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        list_all = "all"
        list_items = "description, note, owner, contact, url, reference_url, code, effective_date, stop_date, state"
        a_few_items = "note, contact"
 
        print "TEST THAT YOU CAN SHOW OR HIDE FIELDS/ELEMENTS IN CREATE NEW OBJECT MODAL."
        
        # fill in mandatory fields only
        do.openCreateNewObjectWindowFromLhn("Market")
 
        # hide_all, show_all, then hide individual
        do.hideInNewModal(list_all, True, "market")
        do.hideInNewModal(list_all, False, "market")
        
        # hide individually
        do.hideInNewModal(list_items, True)
                
        # show all again, hide a few will cause show_all to display, now reshow_all
        do.hideInNewModal(list_all, False, "market")
        do.hideInNewModal(a_few_items, True, "market")
        do.hideInNewModal(list_all, False, "market")
        
        do.populateNewObjectData(do.generateNameForTheObject("market"))
        do.saveNewObjectAndWait()
        do.clickInfoPageEditLink()
               
        # now start testing hide/show after clicking on the Edit link
        do.hideInNewModal(list_all, True, "market")
        do.hideInNewModal(list_all, False, "market")         
        do.hideInNewModal(a_few_items, True, "market")
        do.hideInNewModal(list_all, False, "market") 


if __name__ == "__main__":
    unittest.main()