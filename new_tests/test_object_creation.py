# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: asakhare@google.com
# Maintained By: asakhare@google.com

import logging

from helpers.Helpers import Helpers
from helpers.WebdriverUtilities import WebdriverUtilities
from helpers.testcase import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestObjectCreation(WebDriverTestCase):


    def test_object_creation(self):

        '''Intialization & Setup'''

        self.testname="CreateObjectTests"    # name the test case
        self.setup()                          # do the setup
        do = Helpers()                        # instantiate Helpers class
        util = WebdriverUtilities()           # instantiate utilities class and pass it to Helper object (can remove complexity by inheritance etc and can use seleniumwrapper)
        util.setDriver(self.driver)
        do.setUtils(util)
        do.login()                            # login into the system


        '''Test case'''

        object_list = ["People"]
        #object_list = ["Program", "Contract","Control","DataAsset","Facility","Market","Objective","OrgGroup","Policy","Process","Product",
        #               "Project","Regulation","System","Standard","Clause"]

        for obj in object_list:
            obj_title = do.createObject(obj)
            title = self.driver.find_element_by_css_selector(".row-fluid.wrap-row:first-child .span6:first-child h3").text
            self.assertEqual(title, obj_title)


if __name__ == "__main__":
    unittest.main()