from helperRecip.WebdriverUtilities import WebdriverUtilities
import config
import unittest
from helperRecip.testcase import WebDriverTestCase
from helperRecip.Elements import Elements as elem
from helperRecip.Helpers import Helpers
import time


class ObjectCreationPage(unittest.TestCase):
    util = WebdriverUtilities()
    def createObject(self, grc_object, object_name="", private_checkbox="unchecked", open_new_object_window_from_lhn=True, owner=""):
        print "Start creating object: " + grc_object
        self.closeOtherWindows()
        if object_name == "":
            grc_object_name = self.generateNameForTheObject(grc_object)
        else:
            grc_object_name = object_name   
        
        # in the standard create object flow, a new window gets open via Create link in the LHN, in audit tests the new object gets created via + link, and that's why
        # openCreateNewObjectWindowFromLhn have to be skipped
        if open_new_object_window_from_lhn:           
            self.openCreateNewObjectWindowFromLhn(grc_object) 
        
        self.populateNewObjectData(grc_object_name, owner)      
        
        if private_checkbox == "checked":
            self.util.clickOn(elem.modal_window_private_checkbox)
        self.saveNewObjectAndWait()
        # in the standard create object flow, verify the new object is created happens vi LHN, for audits tests this verification should happen in the mapping modal window
        if open_new_object_window_from_lhn:
            # uncheck box if it is checked
            # self.uncheckMyWorkBox()
            last_created_object_link = self.verifyObjectIsCreatedinLHN(grc_object, grc_object_name)
            time.sleep(5)
            return last_created_object_link
        else:
            print "verifying create object in mapping window"
            time.sleep(5)
            # commented the verification for now
            last_created_object_link = self.verifyObjectIsCreatedInSections(grc_object_name)
        print "Object created successfully."
        