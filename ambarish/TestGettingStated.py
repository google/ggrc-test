__author__ = 'asakhare'

from helperRecip.Elements import Elements
from helperRecip.Helpers import Helpers
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.testcase import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class TestAmb(WebDriverTestCase):


    def test_getting_started(self):

        '''Intialization & Setup'''

        self.testname="TestContractCreate"    # name the test case
        self.setup()                          # do the setup
        do = Helpers()                        # instantiate Helpers class
        util = WebdriverUtilities()           # instantiate utilities class and pass it to Helper object (can remove complexity by inheritance etc and can use seleniumwrapper)
        util.setDriver(self.driver)
        do.setUtils(util)
        do.login()                            # login into the system


        '''Test case'''

        object_title =do.createObject("Contract")
        title = self.driver.find_element_by_css_selector(".row-fluid.wrap-row:first-child .span6:first-child h3").text
        print "title is ", title
        self.assertEqual(title, object_title)


if __name__ == "__main__":
    unittest.main()