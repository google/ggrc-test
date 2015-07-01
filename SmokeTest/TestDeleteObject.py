'''
Created on April 21, 2015

@author: Ambarish
'''


import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *

class TestDeleteObject(WebDriverTestCase):

    def testDeleteObject(self):
        self.testname="TestDeleteObject"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()
        
        do.clickActiveTab()
 #       filterText =do.getFilterText()
#        self.assertEqual('Filter', filterText, filterText)


if __name__ == "__main__":
    unittest.main()