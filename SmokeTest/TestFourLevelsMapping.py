'''
Created on Jul 14, 2014

@author: uduong
'''
import time
import unittest

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestFourLevelsMapping(WebDriverTestCase):

    def testFourLevelsMapping(self):
        self.testname="TestFourLevelsMapping"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        # mapping and un-mapping up to 3 levels: 
        # Program->Regulation->Section->Object
        titlePol = do.getUniqueString("policy")
        titlePrgm = do.getUniqueString("program")
        titleSec = do.getUniqueString("section")
        titleMkt = do.getUniqueString("policy")

        do.createObject("Policy", titlePol)
        do.createObject("Program", titlePrgm)
        do.mapAObjectWidget("Policy", titlePol)
        
        do.createObject("Market", titleMkt)         
        do.createObject("Section", titleSec)
        do.mapAObjectWidget("Market", titleMkt)
                  
        
        do.mapAObjectWidget("Section", titleSec)
              




if __name__ == "__main__":

    unittest.main()