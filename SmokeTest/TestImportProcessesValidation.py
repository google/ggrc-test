'''
Created on Jul 21, 2013

@author: ukyo.duong

Description:  Validate import file when each import file has different error

'''

import time
import unittest

from helperRecip.Elements import Elements
from helperRecip.Helpers import Helpers
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.testcase import *


class TestImportProcessesValidation(WebDriverTestCase):
          
    def testImportProcessesValidation(self):
        noRow = config.file_download_path + "PROCESSES_NO_ROW.csv"
        wrongType = config.file_download_path + "PROCESSES_WRONG_TYPE.csv"
        noTitle = config.file_download_path + "PROCESSES_NO_TITLE.csv"
        dupTitle = config.file_download_path + "PROCESSES_DUP_TITLE.csv"
      
        self.testname="TestImportProcessesValidation"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        do.selectMenuInTopRight("Admin Dashboard")
        self.assertFalse(do.importFile("Processes", noRow, False, "Warning: Missing column"), "Fail negative test on file with now data.")   
            
        do.selectMenuInTopRight("Admin Dashboard")        
        self.assertFalse(do.importFile("Processes", wrongType, False, "Warning: Type must be"), "Fail negative test on file with wrong data type.")
        self.assertEquals(do.getWrongTypeMessage(),"Type must be \"Processes\"", "Fail to display 'wrong type' message.")
         
        do.selectMenuInTopRight("Admin Dashboard")        
        self.assertTrue(do.importFile("Processes", noTitle, True), "Fail negative test on file with no title.")
        self.assertEquals(do.getImportFailedMessage(), "Import failed.", "Fail to display 'Import failed' message.")

if __name__ == "__main__":
    unittest.main()
