'''
Created on Aug 6, 2014

@author: uduong

Description: Object editor role can create object of any types but not "program" and "audit".

WARNING:  With admin to log in and zeroize the email "user44world@gmail.com" so this test can run the next time.

'''

from helpers.Elements import Elements
from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *


class TestCreatePersonObjectEditorLogInOut(WebDriverTestCase):
    
    
    def testCreatePersonObjectEditorLogInOut(self):
        self.testname="TestCreatePersonObjectEditorLogInOut"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        do = Helpers(self)
        do.setUtils(util)
        do.login()

        # ***************************** run this block of codes if run locally *****************************
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
            do.assignUserRole("ObjectEditor")
               
            # now log out and then log in with the new account and try to create a program
            oldEmail = "Example user"
            oldName = "user@example.com"
            absFilePath = expanduser("~") + "/ggrc-core/src/ggrc/login/noop.py"
            do.changeUsernameEmail(oldName, aName, oldEmail, aEmail, absFilePath)
            do.selectMenuInTopRight("Logout")
               
            # Refresh the page
            do.refresh()
               
            # Log in with new user
            do.login()
            print "Log in as : " + do.whoAmI()
            
            object_list = ["Workflow", "Vendor", "Regulation", "Policy", "Standard", "Contract", "Clause", "Section",
                           "Section", "Objective", "Control", "Person", "OrgGroup", "System","Process", "DataAsset",
                           "Product", "Project", "Facility", "Market", "Program", "Audit"]
            
            # since it's an object editor role, the Create New button won't show for certain types
            for object in object_list:
                
                if object=="Program" or object=="Audit":
                    do.assertFalse(do.doesCreateNewExist(object), "Create New button exists for " + str(object))
                else:
                    do.assertTrue(do.doesCreateNewExist(object), "Create New button does not exist for " + str(object))
            
            # should be able to create an object that is not Program or Audit
            last_created_object_link = do.createObject("Contract")
            object_name = str(do.util.getTextFromXpathString(last_created_object_link)).strip()
            self.assertTrue(do.partialMatch("contract-auto-test", object_name), "Fail to match contract name.")
            
            # Restore old login information
            do.changeUsernameEmail(aName, oldName, aEmail, oldEmail, absFilePath)
            do.selectMenuInTopRight("Logout")  
        #   ******************* execute this else block of codes if not run locally *******************
        else: 
            print "Executing the block of codes for non-local ..."
            aEmail = config.editor2
            aName = do.getUniqueString("name")
            aCompany = do.getUniqueString("company")
       
            do.selectMenuInTopRight("Admin Dashboard")
            do.selectMenuItemInnerNavDashBoard("People") 
            do.addPersonInAdminDB(aName, aEmail, aCompany)
            self.assertTrue(do.searchPersonInAdminDB(aName), "Fail searching for newly created person in Admin Dashboard.")
                     
            # edit person authorization
            do.selectMenuItemInnerNavDashBoard("People") # on the roles selection      
            do.clickOnEditAuthorization(aName)
            do.assignUserRole("ObjectEditor")
               
            # now log out and then log in with the new account and try to create a program
            do.selectMenuInTopRight("Logout")
               
            # Refresh the page
            do.refresh()
               
            # Log in with new user
            do.login(aEmail, config.password)
            print "Log in as : " + do.whoAmI()
            
            object_list = ["Workflow", "Vendor", "Regulation", "Policy", "Standard", "Contract", "Clause", "Section",
                           "Section", "Objective", "Control", "Person", "OrgGroup", "System","Process", "DataAsset",
                           "Product", "Project", "Facility", "Market", "Program", "Audit"]
            
            # since it's an object editor role, the Create New button won't show for certain types
            
            for object in object_list:
                
                do.ensureLHNSectionExpanded(object)
                
                if object=="Program" or object=="Audit":
                    do.assertFalse(do.doesCreateNewExist(object), "Create New button exists for " + str(object))
                else:
                    do.assertTrue(do.doesCreateNewExist(object), "Create New button does not exist for " + str(object))
            
            # should be able to create an object that is not Program or Audit
            last_created_object_link = do.createObject("Contract")
            object_name = str(do.util.getTextFromXpathString(last_created_object_link)).strip()
            self.assertTrue(do.partialMatch("contract-auto-test", object_name), "Fail to match contract name.")
            
            if "localhost" in config.url:
                # Restore old login information
                do.changeUsernameEmail(aName, oldName, aEmail, oldEmail, absFilePath)
                do.selectMenuInTopRight("Logout")      
        
if __name__ == "__main__":
    unittest.main()