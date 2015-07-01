'''
Created on Oct 21, 2014

@author: uduong
'''

import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.WorkFlowHelper import WorkFlowHelper
from helpers.testcase import *


class TestHideOnWorkflowModal(WebDriverTestCase):

    def testHideOnWorkflowModal(self):
        self.testname="TestHideOnWorkflowModal"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = WorkFlowHelper(self)
        do.setUtils(util)
        do.login()
        
        list_all = "all"
        list_items = "description, owner, frequency, first_taskgroup, custom_email_message"

        print "TEST THAT YOU CAN SHOW OR HIDE FIELDS/ELEMENTS ON WORKFLOW MODAL."
        
        do.openCreateNewObjectWindowFromLhn("Workflow")
        do.hideInWorkflowNewModal(True, list_all)
        do.hideInWorkflowNewModal(False, list_all)
        do.hideInWorkflowNewModal(True, list_items)
        

if __name__ == "__main__":
    unittest.main()

