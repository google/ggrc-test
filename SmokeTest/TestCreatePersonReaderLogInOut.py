'''
Created on Aug 1, 2014

@author: uduong

Description: Reader can view and work on his assignment but cannot create object or does other admin work.

'''

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestCreatePersonReaderLogInOut(WebDriverTestCase):
    
    
    def testCreatePersonReaderLogInOut(self):
        self.testname="TestCreatePersonReaderLogInOut"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        # run this block of codes if run locally
        if "localhost" in config.url:
            print "Executing the block of codes locally ..."
            aEmail = "auto_email_" + str(do.getRandomNumber(65535)) + "@gmail.com"
            aName = do.getUniqueString("name")
            aCompany = do.getUniqueString("company")
      
            do.selectMenuInTopRight("Admin Dashboard")
            do.selectMenuItemInnerNavDashBoard("People") 
            do.addPersonInAdminDB(aName, aEmail, aCompany)
            self.assertTrue(do.searchPersonInAdminDB(aName), "Fail searching for newly created person in Admin Dashboard.")
      
              
            # edit person authorization
            do.selectMenuItemInnerNavDashBoard("People") # on the roles selection      
            do.clickOnEditAuthorization(aName)
            do.assignUserRole("Reader")
              
            # now log out and then log in with the new account and try to create a program
            oldEmail = "user@example.com"
            oldName = "Example User"
            absFilePath = expanduser("~") + "/ggrc-core/src/ggrc/login/noop.py"
            do.changeUsernameEmail(oldName, aName, oldEmail, aEmail, absFilePath)
            do.selectMenuInTopRight("Logout")
              
            # Refresh the page
            do.refresh()
              
            # Log in with new user
            do.login()
            print "Log in as : " + do.whoAmI()
            
            object_list = ["Vendor", "Regulation", "Policy", "Standard", "Contract", "Clause", "Section",
                           "Section", "Objective", "Control", "Person", "OrgGroup", "System","Process", "DataAsset",
                           "Product", "Project", "Facility", "Market", "Program", "Audit"]
            
            # since it's a reader role, the Create New button won't show
            for object in object_list:
                do.assertFalse(do.doesCreateNewExist(object), "Create New button exists for " + str(object))
     
            print "hi"
            
            # Restore old login information
            do.changeUsernameEmail(aName, oldName, aEmail, oldEmail, absFilePath)
            do.selectMenuInTopRight("Logout")
        else:
            print "Executing the block of codes for non-local ..."            
            aEmail = config.reader2
            aName = do.getUniqueString("name")
            aCompany = do.getUniqueString("company")
      
            do.selectMenuInTopRight("Admin Dashboard")
            do.selectMenuItemInnerNavDashBoard("People") 
            do.addPersonInAdminDB(aName, aEmail, aCompany)
            self.assertTrue(do.searchPersonInAdminDB(aName), "Fail searching for newly created person in Admin Dashboard.")
      
              
            # edit person authorization
            do.selectMenuItemInnerNavDashBoard("People") # on the roles selection      
            do.clickOnEditAuthorization(aName)
            do.assignUserRole("Reader")
              
            # now log out and then log in with the new account and try to create a program
            do.selectMenuInTopRight("Logout")
              
            # Refresh the page
            do.refresh()
              
            # Log in with new user
            do.login(aEmail, config.same_password)
            print "Log in as : " + do.whoAmI()
            
            # Workflow is left out on purpose because Create New is there but reader can't create object anyway
            object_list = ["Vendor", "Regulation", "Policy", "Standard", "Contract", "Clause", "Section",
                           "Section", "Objective", "Control", "Person", "OrgGroup", "System","Process", "DataAsset",
                           "Product", "Project", "Facility", "Market", "Program", "Audit"]
            
            # since it's a reader role, the Create New button won't show
            for object in object_list:
                do.ensureLHNSectionExpanded(object)
                do.assertFalse(do.doesCreateNewExist(object), "Create New button exists for " + str(object))          
               
        
if __name__ == "__main__":
    unittest.main()
