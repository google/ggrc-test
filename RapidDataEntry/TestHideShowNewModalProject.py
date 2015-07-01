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


class TestHideShowNewModalProject(WebDriverTestCase):

    def testHideShowNewModalProject(self):
        self.testname="TestHideShowNewModalProject"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        list_all = "all"
        list_items = "description, note, owner, contact, url, reference_url, code, effective_date, stop_date, state"
        a_few_items = "url, effective_date, stop_date, state"
 
        print "TEST THAT YOU CAN SHOW OR HIDE FIELDS/ELEMENTS IN CREATE NEW OBJECT MODAL."
        
        # fill in mandatory fields only
        do.openCreateNewObjectWindowFromLhn("Project")
 
        # hide_all, show_all, then hide individual
        do.hideInNewModal(list_all, True, "project")
        do.hideInNewModal(list_all, False, "project")
        
        # hide individually
        do.hideInNewModal(list_items, True)
                
        # show all again, hide a few will cause show_all to display, now reshow_all
        do.hideInNewModal(list_all, False, "project")
        do.hideInNewModal(a_few_items, True, "project")
        do.hideInNewModal(list_all, False, "project")
        
        do.populateNewObjectData(do.generateNameForTheObject("project"))
        do.saveNewObjectAndWait()
        do.clickInfoPageEditLink()
               
        # now start testing hide/show after clicking on the Edit link
        do.hideInNewModal(list_all, True, "project")
        do.hideInNewModal(list_all, False, "project")         
        do.hideInNewModal(a_few_items, True, "project")
        do.hideInNewModal(list_all, False, "project") 


if __name__ == "__main__":
    unittest.main()