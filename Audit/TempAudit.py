'''
Created on Oct 30, 2013

@author: diana.tzinov
'''
'''
Created on Sep 10, 2013

@author: diana.tzinov
'''




import unittest
import time
import os
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers
from helperRecip.GRCObject import GRCObject
import time,  calendar
import datetime
from datetime import timedelta
from datetime import date



class TestProgramAudit(WebDriverTestCase):

    
    def testProgramAudit(self):
        self.testname="TestProgramAudit"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers()
        do.setUtils(util)
        do.login()

        #
        # Read audit_setup_data to retrieve program name and the IDs of the 3 objectives
        #
        objectiveID={}
        f=open("audit_setup_data","r")
        program_name=f.readline().strip("\n")
        ##objectiveID[0]=int(f.readline().strip("\n"))
        #objectiveID[1]=int(f.readline().strip("\n"))
        #objectiveID[2]=int(f.readline().strip("\n"))
        #print program_name
        #print objectiveID
        
        
        util.switchToNewUrl("https://grc-test.appspot.com/programs/949#audit_widget")
        # 1.  Navigate to the Program page created in Audit Part 1
        #first_program_in_lhn = '//ul[@class="top-level"]//li[contains(@data-model-name,"Program")]//li[contains(.,"NAME")]/a'.replace("NAME", program_name)
        #print first_program_in_lhn
        #do.navigateToObjectWithSearch(program_name,"Program")
        
        
        # 2.  Choose Audit from Object page nav to bring up the Audit widget
        #do.navigateToAuditSectionViaInnerNavSection("Audit")

        # 3.  Hover over blue +Audit link in widget, link changes to Create Audit - Click on Create Audit to open modal
        #util.hoverOverAndWaitFor(element.audit_area_plus_audit_link, element.audit_area_create_audit_link)
        #util.clickOn( element.audit_area_create_audit_link)
                     
        # 4.  New Audit (modal)
        #new_audit_title = do.createAudit(program_name)
        
        # 5.  Confirm the audit appear in the widget
        newly_created_audit = element.audit_area_created_audit.replace("AUDIT_TITLE", "2013: program - Audit")
        """
        print newly_created_audit
        util.waitForElementToBePresent(newly_created_audit)
        self.assertTrue(util.isElementPresent(newly_created_audit), "do not see the newly created audit " +"2013: program - Audit" )
        
        # 6. Click on it to open the 2nd tier info.  confirm there are 3 requests in the PBC Requests section. 
        newly_created_audit_open_link  = element.audit_area_created_audit_open_link.replace("AUDIT_TITLE", "2013: program - Audit")
        print newly_created_audit_open_link
        util.waitForElementToBePresent(newly_created_audit_open_link)
        self.assertTrue(util.isElementPresent(newly_created_audit_open_link), "do not see the newly created audit open link "  )
        util.clickOn(newly_created_audit_open_link)
        util.switch_to_active_element()
        """
        util.max_screen()
        #newly_created_audit_open_link  = element.audit_area_created_audit_open_link.replace("AUDIT_TITLE", "2013: program - Audit")
        #util.clickOn(newly_created_audit_open_link)
        #verifying the 3 objectives
        """
        for objective_title in grcobject.objective_title:
            objective_title_element = element.audit_pbc_request.replace("TITLE", objective_title)
            print objective_title_element
            util.waitForElementToBePresent(objective_title_element)
            self.assertTrue(util.isElementPresent(objective_title_element), "do not see the pbc request " + objective_title_element )
        
        #7. Change Objective 2 for Auto test of Audit - Type: Interview
        print "Change Objective 2 for Auto test of Audit - Type: Interview"
        objective2_select = element.audit_pbc_request_type_select.replace("TITLE",grcobject.objective_title[1] )
        util.waitForElementToBePresent(objective2_select)
        util.selectFromDropdownUntilSelected(objective2_select,  "Interview")
        #click on "Objective 2 for Auto test of Audit" to open 2nd tier info
        print "click on Objective 2 for Auto test of Audit to open 2nd tier info"
        do.expandCollapseRequest(grcobject.objective_title[1])
        #click on Edit PBC Response
        util.waitForElementToBePresent(element.audit_pbc_request_expanded_content_edit_link)
        self.assertTrue(util.isElementPresent(element.audit_pbc_request_expanded_content_edit_link), "do not see the Edit link in the expanded request  "  )
        #click on Response to open that 2nd tier info
        response_element = element.audit_pbc_request_response.replace("TITLE",grcobject.objective_title[1] )
        print "response element " + response_element
        util.waitForElementToBePresent(response_element)
        self.assertTrue(util.isElementPresent(response_element), "do not see the Respond element in the expanded Request section for  "+ grcobject.objective_title[1]   )
        print "expanding response and Edit PBC Response "
        util.clickOn(response_element) #to expand the response
        util.waitForElementToBePresent(element.audit_pbc_request_expanded_response_edit_link)
        self.assertTrue(util.isElementPresent(element.audit_pbc_request_expanded_response_edit_link), "do not see the Edit PBS Response link in the expanded Request section for  "+ grcobject.objective_title[1]   )
        util.clickOn(element.audit_pbc_request_expanded_response_edit_link)
        #Delete
        print "deleting Response"
        do.deleteObject()
        #collapse back the request
        print "collapse back the request"
        do.expandCollapseRequest(grcobject.objective_title[1])
        time.sleep(3)
        util.selectFromDropdownUntilSelected(objective2_select,  "Interview")
        time.sleep(3)
        
         #8. Change Objective 3 for Auto test of Audit - Type: Population Sample
        objective3_select = element.audit_pbc_request_type_select.replace("TITLE",grcobject.objective_title[2] )
        util.waitForElementToBePresent(objective3_select)
        print "Change Objective 3 for Auto test of Audit - Type: Population Sample"
        #util.selectFromDropdownUntilSelected(objective3_select,  "Population Sample")
        #click on "Objective 3 for Auto test of Audit" to open 2nd tier info
        
        do.expandCollapseRequest(grcobject.objective_title[2])
        #click on Edit PBC Response
        util.waitForElementToBePresent(element.audit_pbc_request_expanded_content_edit_link)
        self.assertTrue(util.isElementPresent(element.audit_pbc_request_expanded_content_edit_link), "do not see the Edit link in the expanded request  "  )
        #click on Response to open that 2nd tier info
        response_element = element.audit_pbc_request_response.replace("TITLE",grcobject.objective_title[2] )
        print "response element " + response_element
        util.waitForElementToBePresent(response_element)
        self.assertTrue(util.isElementPresent(response_element), "do not see the Respond element in the expanded Request section for  "+ grcobject.objective_title[2]   )
        print "expanding response and Edit PBC Response "
        util.clickOn(response_element) #to expand the response
        util.waitForElementToBePresent(element.audit_pbc_request_expanded_response_edit_link)
        self.assertTrue(util.isElementPresent(element.audit_pbc_request_expanded_response_edit_link), "do not see the Edit PBS Response link in the expanded Request section for  "+ grcobject.objective_title[2]   )
        util.clickOn(element.audit_pbc_request_expanded_response_edit_link)
        #Delete
        print "deleting Response"
        do.deleteObject()
        #collapse back the request
        print "collapse back the request"
       
        do.expandCollapseRequest(grcobject.objective_title[2])
        time.sleep(5)
        util.selectFromDropdownUntilSelected(objective3_select,  "Population Sample")
        
        #taking a screenshot
        util.switch_to_active_element()
        util.get_a_screen_shot("test_screenshot.png")
        
        #9.    Click on Objective 1 for Auto Test of Audit to open 2nd tier info (Documentation Response)
        do.expandCollapseRequest(grcobject.objective_title[0])
        response_element = element.audit_pbc_request_response.replace("TITLE",grcobject.objective_title[0] )
        print "response element " + response_element
        #util.waitForElementToBePresent(element.audit_pbc_request_expanded_content_response_email_inputfield)
        util.waitForElementValueToBePresent(response_element)
        
        self.assertTrue(util.isElementPresent(response_element), "can't see the expanded contetnt for the request link") 
        util.waitForElementToBePresent(response_element)
        #self.assertTrue(util.isElementPresent(element.audit_pbc_request_response), "do not see the firts response presented")
            
       
        #.    Assign that Response to another team member (jeff@reciprocitylabs.com is fine)
        response_email_inputfield = element.audit_pbc_request_expanded_content_response_email_inputfield.replace("TITLE",grcobject.objective_title[0] )
        print "response_email_inputfield " + response_email_inputfield
        util.waitForElementToBePresent(response_email_inputfield)
        self.assertTrue(util.isElementPresent(response_email_inputfield), "do not see the firts response owner email textfield presented")
        util.inputTextIntoField("jeff@reciprocitylabs.com", response_email_inputfield)
        
        #Click on the response header to open the response
        open_response_link = element.audit_pbc_request_response_expand_collapse_link.replace("TITLE",grcobject.objective_title[0] )
        util.waitForElementToBePresent(open_response_link)
        self.assertTrue(util.isElementPresent(open_response_link), "do not see the open close button for the response")
        util.clickOn(open_response_link)
        
        #click +Object to open Map Object Selector. 
        add_object_link = element.audit_pbc_request_response_add_object_link.replace("TITLE",grcobject.objective_title[0] )
        util.waitForElementToBePresent(add_object_link)
        self.assertTrue(util.isElementPresent(add_object_link), "do not see the open close button for the response")
        util.clickOn(add_object_link)
        
        #Change top filter to Org Group. 
        util.waitForElementToBePresent(element.mapping_modal_window)
        self.assertTrue(util.isElementPresent(element.mapping_modal_window), "do not see the modal window")
        util.waitForElementToBePresent(element.mapping_modal_top_filter_selector_dropdown)
        self.assertTrue(util.isElementPresent(element.mapping_modal_top_filter_selector_dropdown), "do not see the modal window")
        util.selectFromDropdownByValue(element.mapping_modal_top_filter_selector_dropdown, "OrgGroup")
        
        #Choose Reciprocity Dev Team and hit Map button. (use search to find this if easier to implement)
        util.waitForElementToBePresent(element.mapping_modal_top_filter_selector_dropdown_reciprocity_dev_team_option)
        self.assertTrue(util.isElementPresent(element.mapping_modal_top_filter_selector_dropdown_reciprocity_dev_team_option), "do not see the open close button for the response")
        util.clickOn(element.mapping_modal_top_filter_selector_dropdown_reciprocity_dev_team_option)
        util.waitForElementToBePresent(element.mapping_modal_window_map_button)
        self.assertTrue(util.isElementPresent(element.mapping_modal_window_map_button), "no Map button")
        util.clickOn(element.mapping_modal_window_map_button)
        util.waitForElementNotToBePresent(element.mapping_modal_window)
        
         #Confirm Reciprocity Dev Team is mapped to the Response and appears in the area provided
        util.waitForElementToBePresent(element.audit_pbc_request_response_mapped_org_group_object_withrecipprocity_dev_team)
        self.assertTrue(util.isElementPresent(element.audit_pbc_request_response_mapped_org_group_object_withrecipprocity_dev_team), "no Mapped org group button")
        
        #Click +Upload Evidence in the Evidence area to open the file picker
        upload_evidence_link = element.audit_pbc_request_response_upload_evidence_link.replace("TITLE",grcobject.objective_title[0] )
        util.waitForElementToBePresent(upload_evidence_link)
        self.assertTrue(util.isElementPresent(upload_evidence_link), "no Upload Evidence link")
        util.clickOn(upload_evidence_link)
        util.waitForElementToBePresent('//iFrame[@class="picker-frame picker-dialog-frame"]')
        #self.assertTrue(util.isElementPresent('//iFrame[@class="picker-frame picker-dialog-frame"]'), "no Upload window")
        url=util.getAnyAttribute('//iFrame[@class="picker-frame picker-dialog-frame"]', "src")
        print url
        util.switchToNewUrl(url)
        file_is = os.getcwd() + "/test_screenshot.png"
        util.uploadItem(file_is, element.select_file_button)
        util.waitForElementToBeVisible(element.upload_file_button)
        util.find_element_by_xpath(element.upload_file_button).click() 
        time.sleep(10) # wait for uploading the file
        util.backBrowser()
        util.refreshPage()
        """
        #waiting to audit to appear back
        newly_created_audit = element.audit_area_created_audit.replace("AUDIT_TITLE", "2013: program - Audit")
        print newly_created_audit
        util.waitForElementToBePresent(newly_created_audit)
        self.assertTrue(util.isElementPresent(newly_created_audit), "do not see the newly created audit " +"2013: program - Audit" )
         
        newly_created_audit_open_link  = element.audit_area_created_audit_open_link.replace("AUDIT_TITLE", "2013: program - Audit")
        print newly_created_audit_open_link
        util.waitForElementToBePresent(newly_created_audit_open_link)
        self.assertTrue(util.isElementPresent(newly_created_audit_open_link), "do not see the newly created audit open link "  )
        util.clickOn(newly_created_audit_open_link)
        """
        util.switch_to_active_element()
        #expand objetiive 1 to verify the uploaded file
        do.expandCollapseRequest(grcobject.objective_title[0])
        evidence_folder_link = element.audit_pb_request_response_evidence_folder_link.replace("TITLE",grcobject.objective_title[0] )
        util.waitForElementToBePresent(evidence_folder_link)
        self.assertTrue(util.isElementPresent(evidence_folder_link), "do not see the evidene folder link "  )
        do.expandCollapseRequest(grcobject.objective_title[0])
        """
        #10.  Click on Objective 2 for Auto Test of Audit to open 2nd tier info (Interview)

        print "click on Objective 2 for Auto test of Audit to open 2nd tier info"
        do.expandCollapseRequest(grcobject.objective_title[1])
        """
        objective2_select = element.audit_pbc_request_type_select.replace("TITLE",grcobject.objective_title[1] )
        util.waitForElementToBePresent(objective2_select)
        util.selectFromDropdownUntilSelected(objective2_select,  "Interview") # didn't work the first time
        print "Hover over +PBC Request then click on Create PBC Response to launch modal"
        add_pbc_response_link_within_the_objective = element.audit_pbc_request.replace("TITLE",grcobject.objective_title[1] )+element.section_add_link
        create_pbc_response_link_within_the_objective = element.audit_pbc_request.replace("TITLE",grcobject.objective_title[1] )+element.section_create_link
        util.waitForElementToBePresent(add_pbc_response_link_within_the_objective)
        util.scrollIntoView(add_pbc_response_link_within_the_objective)
        util.hoverOverAndWaitFor(add_pbc_response_link_within_the_objective,create_pbc_response_link_within_the_objective)
        util.clickOn(add_pbc_response_link_within_the_objective)
        util.clickOn(create_pbc_response_link_within_the_objective)
        #Description field :  "Response foir Interview Type", Save
        print "creating new interview response"
        do.NewResponseCreate("Response for Interview Type")
        #Click on Response for Interview Type header to reveal response 2nd tier info
      
         #click +Object to open Map Object Selector.  Change top filter to Org Group if neccessary (should not be).  Choose Reciprocity Dev Team and hit Map button. (use search to find this if easier to implement)
         #Confirm Reciprocity Dev Team is mapped to the Response and appears in the area provided

        
        
        #after creating a new response, the whole response section gets expanded automatically now, 
        #just need to wait for all elements to load (+Object, +Person, + Meeting)
        
        add_object_link = element.audit_pbc_request_response_add_object_link_within_response.replace("TITLE",grcobject.objective_title[1] )
        add_person_link = element.audit_pbc_request_response_add_person_within_response.replace("TITLE",grcobject.objective_title[1] )
        add_meeting_link = element.audit_pbc_request_response_add_meeting.replace("TITLE",grcobject.objective_title[1] )
        util.waitForElementToBePresent(add_object_link)
        self.assertTrue(util.isElementPresent(add_object_link), "do not see the open close button for the response")
        util.waitForElementToBePresent(add_person_link)
        self.assertTrue(util.isElementPresent(add_person_link), "do not see the + Person link")
        util.waitForElementToBePresent(add_meeting_link)
        self.assertTrue(util.isElementPresent(add_meeting_link), "do not see the + Meeting link")
        
        #click +Object to open Map Object Selector. 
        util.clickOn(add_object_link)
         
        #Change top filter to Org Group. 
        util.waitForElementToBePresent(element.mapping_modal_window)
        self.assertTrue(util.isElementPresent(element.mapping_modal_window), "do not see the modal window")
        util.waitForElementToBePresent(element.mapping_modal_top_filter_selector_dropdown)
        self.assertTrue(util.isElementPresent(element.mapping_modal_top_filter_selector_dropdown), "do not see the modal window")
        util.selectFromDropdownByValue(element.mapping_modal_top_filter_selector_dropdown, "OrgGroup")
        
        #Choose Reciprocity Dev Team and hit Map button. (use search to find this if easier to implement)
        util.waitForElementToBePresent(element.mapping_modal_top_filter_selector_dropdown_reciprocity_dev_team_option)
        self.assertTrue(util.isElementPresent(element.mapping_modal_top_filter_selector_dropdown_reciprocity_dev_team_option), "do not see the open close button for the response")
        util.clickOn(element.mapping_modal_top_filter_selector_dropdown_reciprocity_dev_team_option)
        util.waitForElementToBePresent(element.mapping_modal_window_map_button)
        self.assertTrue(util.isElementPresent(element.mapping_modal_window_map_button), "no Map button")
        util.clickOn(element.mapping_modal_window_map_button)
        util.waitForElementNotToBePresent(element.mapping_modal_window)
        
         #Confirm Reciprocity Dev Team is mapped to the Response and appears in the area provided
        util.waitForElementToBePresent(element.audit_pbc_request_response_mapped_org_group_object_withrecipprocity_dev_team)
        self.assertTrue(util.isElementPresent(element.audit_pbc_request_response_mapped_org_group_object_withrecipprocity_dev_team), "no Mapped org group button")
        
        
        #click on +Person link to launch Map People modal
        print "click on +Person link to launch Map People modal"
        #add_person_link = element.audit_pbc_request_response_add_person_within_response.replace("TITLE",grcobject.objective_title[1] )
        util.waitForElementToBePresent(add_person_link)
        self.assertTrue(util.isElementPresent(add_person_link), "do not see the + Person link")
        util.clickOn(add_person_link)
        
        #search for "silas"
        print "searching and mapping another participant"
        person_email=do.mapPerson("silas")
        
        #confirm silas has been added to Participant area
        print "confirming another participant has been mapped"
        participant_email = element.audit_pbc_request_response_participant_email.replace("EMAIL",person_email)
        util.waitForElementToBePresent(participant_email)
        self.assertTrue(util.isElementPresent(participant_email), "do not see the Person Mapped email")
        """
        #click on +Meetings in Meetings area
        util.waitForElementToBePresent('//li[@data-object-type="interview_response"]//div[@data-model="true"]//a[contains(@class,"openclose")]')
        util.clickOn('//li[@data-object-type="interview_response"]//div[@data-model="true"]//a[contains(@class,"openclose")]')
        print "click on +Meetings in Meetings area"
        
        add_meeting_link = element.audit_pbc_request_response_add_meeting.replace("TITLE",grcobject.objective_title[1] )
        util.waitForElementToBePresent(add_meeting_link)
        self.assertTrue(util.isElementPresent(add_meeting_link), "do not see +Meeting link")
        util.scrollIntoView(add_meeting_link)
        create_meeting_link = element.audit_pbc_request_response_create_meeting.replace("TITLE",grcobject.objective_title[1] )
        util.hoverOverAndWaitFor(add_meeting_link,create_meeting_link)
        util.clickOn(add_meeting_link)
        util.clickOn(create_meeting_link)
        #util.click_on_link_by_link_text("Meeting")
        
        meeting_date = (date.today())+ datetime.timedelta(days=14)
        meeting_date_into_format = do.convertDateIntoFormat(meeting_date)
        
        #Enter Title:  Auto Test of Audit - Interview Response - Scheduling a meeting, Choose date : current date + 2 weeks, Set start time to 12pm, Set end time to 1pm, Confirm particpants are silas and testrecip
        do.scheduleMeeting("Auto Test of Audit - Interview Response - Scheduling a meeting",meeting_date_into_format, "12:00 PM", "01:00 PM")
        util.focus()
        util.waitForElementToBePresent('//li[@data-object-type="meeting"]//a[contains(@class,"openclose")]')
        util.clickOn('//li[@data-object-type="meeting"]//a[contains(@class,"openclose")]')
        
        #util.switch_to_active_element()
        
        util.isElementPresent('//a[contains(@href,"/calendar/event")]')
        util.isElementPresent('//li[@data-object-type="meeting"]//div[@class="tree-description short"]')
        print util.getTextFromXpathString('//li[@data-object-type="meeting"]//div[@class="tree-description short"]')
        time.sleep(3)
        do.expandCollapseRequest(grcobject.objective_title[1])
        
        time.sleep(3)
        do.expandCollapseRequest(grcobject.objective_title[2])
        
        
        #google_meeting_time = util.getTextFromXpathString(element.google_meeting_title)
        #print google_meeting_time
        
        #util.clickOn(open_response_link)
        #Click on the response header to open the response
        """
        # C.    Click on +PBC Response link to create a new Documentation Response
        response_add_button = element.audit_pbc_request_expanded_content_add_response_button.replace("TITLE",grcobject.objective_title[0] )
        create_response_button = element.audit_pbc_request_expanded_content_create_response_button.replace("TITLE",grcobject.objective_title[0] )
        print "response_add_button " + response_add_button
        util.waitForElementToBePresent(response_add_button)
        self.assertTrue(util.isElementPresent(response_add_button), "do not see the +PBC Response button")
        print create_response_button
        util.hoverOverAndWaitFor(response_add_button,create_response_button)
        util.clickOn(response_add_button)
        #util.waitForElementToBePresent(create_response_button)
        util.clickOn(create_response_button)
        
        #D.    Enter "This is a documentation response for Objective 1 for Auto Test of Audit Request"
        # E.    Confirm Assignee is populated with Audit lead name

        util.waitForElementToBePresent(element.audit_modal_audit_lead_input_field)
        self.assertTrue(util.isElementPresent(element.audit_modal_audit_lead_input_field), "can't see the Audit Lead input field")
        audit_auto_populated_audit_lead = util.getAnyAttribute(element.audit_modal_audit_lead_input_field,"value")
        self.assertTrue(element.audit_modal_audit_lead_value  in audit_auto_populated_audit_lead,"not correct Audit Lead value")
        do.createResponse( "This is a documentation response for Objective 1 for Auto Test of Audit Request")
        
        
        time.sleep(10)
       """
if __name__ == "__main__":
    unittest.main()