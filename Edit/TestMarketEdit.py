'''
Created on Aug 10, 2013

@author: diana.tzinov
'''



import unittest
import time
from helpers.testcase import *
from helpers.Elements import Elements
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.Helpers import Helpers
from helpers.GRCObject import GRCObject


class TestMarketEdit(WebDriverTestCase):
    
    
    def testMarketEdit(self):
        self.testname="TestMarketEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        grcobject = GRCObject()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("Market")
        object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Market",last_created_object_link)
        do.populateObjectInEditWindow( object_name , grcobject.market_elements, grcobject.market_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.market_elements, grcobject.market_values)
        do.deleteObject()
        
if __name__ == "__main__":
    unittest.main()
