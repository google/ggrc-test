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


class TestProductEdit(WebDriverTestCase):
    
    
    def testProductEdit(self):
        self.testname="TestProductEdit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        grcobject = GRCObject()
        do.setUtils(util)
        do.login()
        last_created_object_link = do.createObject("Product")
        object_name = str(util.getTextFromXpathString(last_created_object_link)).strip()
        do.navigateToObjectAndOpenObjectEditWindow("Product",last_created_object_link)
        do.populateObjectInEditWindow( object_name , grcobject.product_elements, grcobject.product_values)
        do.openObjectEditWindow()
        do.verifyObjectValues(grcobject.product_elements, grcobject.product_values)
        do.deleteObject()
        
if __name__ == "__main__":
    unittest.main()
