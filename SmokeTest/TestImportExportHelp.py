'''
Created on Jan 12, 2015

@author: uduong

Description:  Export a file and and reimport it.

'''

from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestImportExportHelp(WebDriverTestCase):
       
    def testImportExportHelp(self):
        self.testname="TestImportExportHelp"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        do = Helpers(self)
        do.setUtils(util)
        do.login()
     
        # export help
        filePath = config.test_db + "HELP.csv"
        do.selectMenuInTopRight("Admin Dashboard")
        do.exportFile("help", filePath)
   
        # import help
        do.importFile("Processes", filePath)

if __name__ == "__main__":
    unittest.main()
