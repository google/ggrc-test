'''
Created on Jul 17, 2013

@author: diana.tzinov
'''


import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestContractCreate(WebDriverTestCase):
    
    
    def testContractCreate(self):
        self.testname="TestContractCreate"
        self.setup()
        '''
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        '''
        do = Helpers()
        '''
        do = Helpers(self)
        do.setUtils(util)
        '''
        do.login()
        last_created_object_link =do.createObject("Contract")
        do.navigateToObjectAndOpenObjectEditWindow("Contract",last_created_object_link)
        do.deleteObject()
       
        
if __name__ == "__main__":
    unittest.main()
