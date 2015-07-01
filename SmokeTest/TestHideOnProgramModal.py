'''
Created on Oct 22, 2014

@author: uduong
'''


import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *



class TestHideOnProgramModal(WebDriverTestCase):

    def testHideOnProgramModal(self):
        self.testname="TestHideOnProgramModal"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        list_all = "all"
        list_items = "description, private, note, owner, contact, url, reference_url, code, effective_date, end_date, state"
        a_few_items = "owner, note"

        print "TEST THAT YOU CAN SHOW OR HIDE FIELDS/ELEMENTS ON PROGRAM MODAL."
       
        # fill in mandatory fields only
        do.openCreateNewObjectWindowFromLhn("Program")

        # hide_all, show_all, then hide individual
        do.hideInProgramNewModal(True, list_all)
        do.hideInProgramNewModal(False, list_all)
        do.hideInProgramNewModal(True, list_items)
        
        # show all again, hide a few will cause show_all to display, now reshow_all
        do.hideInProgramNewModal(False, list_all)
        do.hideInProgramNewModal(True, a_few_items)
        do.hideInProgramNewModal(False, list_all)
        
        # hide all again
        do.hideInProgramNewModal(True, list_all)


if __name__ == "__main__":
    unittest.main()