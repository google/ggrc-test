'''
Created on May 26, 2014

@author: uduong
@description This class is created to hold all functions related to WorkFlow only.  Elements are also stored locally to the function that uses it.
It's unlikely that elements are used by others when you purposely write it for the specified function.  Also, when Elements and Helpers classes 
are getting bigger they become unmanageable.  

All public functions have "WF" as a post-fix to signify that the function is not from the parent class.

'''

from datetime import datetime
import time

from Elements import Elements as elem
import config
from helpers.Helpers import Helpers, log_time


class WorkFlowHelper(Helpers):
    
    '''
    Any elements that are shared among the functions can go here
    '''

    startWorkflow_bt = '//button[@type="submit" and @href="#workflowStart"]'
    endWorkflow_bt = '//button[@type="submit" and @class="btn end-workflow"]'

    my_wait_time =  10;

    @log_time
    # objecName: Controls or Projects, etc.
    # relevantTo: Program
    def addObjectsWF(self, objectName, relevantTo, whatItem):
        add_object_lk = '//a[@data-original-title="Map Object to this Workflow"]' 
        object_select_drdn = '//select[@id="frequency"]'
        add_selected_bt = '//a[@id="addSelected"]'
        search_txtbx = '//input[@id="search"]'
        map_bt = '//div[@class="confirm-buttons"]/a'
        # check the count first
        
        text = self.countOfAnyObjectLHS("Workflow")
        
        self.util.clickOn(elem.left_nav_object_section_add_button.replace("OBJECT", "Workflow"))
        self.util.selectFromDropdownByValue(object_select_drdn, objectName)
        self.util.inputTextIntoField(whatItem, search_txtbx)
        self.util.clickOn(map_bt)
        
        # TODO no real data is shown so can't progress further
        
        self.util.clickOn(add_selected_bt)

        # wait before checking count
        time.sleep(1)

        countAfter = text = self.countOfAnyObjectLHS("Workflow")

        if countAfter == text+1:

            return True
        else:
            return False

    @log_time
    # Return true if addTask succeed and not error out
    # If taskName is blank, it will auto assign a unique name, e.g, Task-auto + timestamp
    def addTaskWF(self, taskName="", selectAll=False): 
        add_task_lk = '//a[@href="#objectSelector" and @data-mapping="tasks"]' 
        checkboxAll_chbx = '//input[@id="objectAll"]'
        addSelected_bt = '//a[@id="addSelected"]'
        task_table = '//div[@id="objectSelector"]/div[@class="results"]//ul'

        if selectAll == True:
            self.util.clickOn(addSelected_bt)  # just click on the button
        else:
            self.util.clickOn(checkboxAll_chbx)  # it's checked by default so click to uncheck it

            count = self.util.countChildren(task_table) 
            print "DEBUG, count: " + count

            for x in range(2, count):
                xpath = task_table + '/li[' + x + ']//div[@class="tree-title-area"]/i'
                title = self.util.getTextFromXpathString(xpath)
                print "DEBUG, title: " + title
                if title == taskName:  # if found, click on the checkbox next to it
                    self.util.clickOn(task_table + '//input[@type="checkbox"]')  # check it
                    break  # get out
        
        self.util.clickOn(addSelected_bt)
        return True

    @log_time
    # Create a new task from a window popped up by "add task" and return the task name if in auto create mode
    # Pre-condition: the window must already be up
    # To test the Cancel feature, set save=False
    def createNewTaskWF(self, title="", detail_description="", save=True):
        create_task_bt = '//a[@class="btn btn-add addTaskModal"]'
        summary_title_txtbx = '//input[@id="task-title"]'
        detail_txtbx = '//div[@id="newTask"]//textarea[@id="program_description"]'
        save_bt = '//a[@id="addTask"]' 
        cancel_bt = '//a[@id="addTask"]/../../../div/div/a[@data-dismiss="modal"]'

        if title == "":
            title = "Task-auto-" + self.getTimeId()

        self.util.clickOn(create_task_bt)
        self.util.inputTextIntoField(title, summary_title_txtbx)
        self.util.inputTextIntoField(detail_description, detail_txtbx)
        if save==True:
            self.util.clickOn(save_bt)
        else:
            self.util.clickOn(cancel_bt)
        return title

    @log_time
    # Return true if addPerson succeed and not error out
    def addPersonWF(self, personName="", selectAll=False):
        add_person_lk = '//a[@href="#objectSelector" and @data-mapping="person"]' 
        checkboxAll_chbx = '//input[@id="objectAll"]'
        addSelected_bt = '//a[@id="addSelected"]'
        task_table = '//div[@id="objectSelector"]/div[@class="results"]//ul'
        if selectAll == True:
            self.util.clickOn(addSelected_bt)  # just click on the button
        else:
            count = self.util.countChildren(task_table) 
            print "count: " + count
            
            for x in range(2, count):
                xpath = task_table + '/li[' + x + ']//div[@class="tree-title-area"]/i'
                title = self.util.getTextFromXpathString(xpath)
                print "title: " + title
                if title == personName:  # if found, click on the checkbox next to it
                    self.util.clickOn(task_table + '//input[@type="checkbox"]')  # check it
                    break  # get out
        self.util.clickOn(addSelected_bt)
        return True

    @log_time
    # Return true if addTaskGroup succeed and not error out
    # if you want to test the Cancel feature then set save=False
    # date format: "2014_05_27", for test purpose please use current date
    def addTaskGroupWF(self, groupName, personName, date, save=True):
        group_txtbx = '//input[@id="new_object_name"]'
        search_txtbox = '//input[@id="new_object_name"]'
        save_bt = '//a[@id="addTaskGroup"]'
        cancel_bt = '//a[@id="cancelTaskGroup"]'
        calendar_picker = '//input[@id="tg_end_date"]'
        month_label = '//div[@id="ui-datepicker-div"]//span[@class="ui-datepicker-month"]'
        year_label = '//div[@id="ui-datepicker-div"]//span[@class="ui-datepicker-year"]'
        date_table = '//table[@class="ui-datepicker-calendar"]/tbody'

        self.util.inputTextIntoField(groupName, group_txtbx)
        self.util.inputTextIntoField(personName, search_txtbox)
        
        if save == True:
            self.util.clickOn(save_bt)
        else:
            self.util.clickOn(cancel_bt)

        day = str(datetime.now())
        
        day = day[8:10]
        
        # dateTable = WebElement(self.driver.findElement(By.TAG_NAME("table")));
        # List<WebElement> tableRows = yourTable.findElements(By.TAG_NAME("tr"));
        
        # just pick the current day from the day table        
        for row in range (1, 5):
            for column in range (1, 7):
                xpath = str(date_table + '/tr[' + row + ']/td[' + column + ']/a')
                theDay = self.util.clickOn(xpath)
                if (day == theDay):
                    self.util.clickOn(xpath)
                    break  # inner loop
                else:
                    continue;

            break  # outer loop

        return True

    @log_time
    def startWorkFlowWF(self, proceed=True):       
        proceed_bt = '//a[@id="confirmStartWorkflow"]'
        cancel_bt = '//a[@id="cancelStartWorkflow"]'
        self.util.clickOn(self.startWorkflow_bt)
        time.sleep(.5)
        if proceed == True:
            self.util.clickOn(proceed_bt)
        else:
            self.util.clickOn(cancel_bt)

    @log_time
    # prerequisite: Already have "Workflow"menu open
    def stopWorkFlowWF(self):
        self.util.clickOn(self.endWorkflow_bt)
        
    ### NOTE:     searchObjectInWidgetPanelWF vs.  searchObjectInAddObjectToWorkflowWind ###
    ###           widget panel is next to inner nav  ###    
        
    @log_time
    # Search for an object in the table.  Return TRUE if found and FALSE otherwise.
    def searchObjectInWidgetPanelWF(self, title, expandItIfFound=False):

        count = self._workflowObjectCount()
        for index in range [1:count]:
            xpath = '//div[@id="filters"]/ul[1]/li[' + index + ']//div[@class="tree-title-area"]'
     
            titleText = self.util.getTextFromXpathString(xpath)
            
            if titleText == title:
                if expandItIfFound == True:
                    self.util.clickOn(xpath)
                    
                return True
            else:
                return False
            
    @log_time
    # Search for the named object and ummap it
    # Return the current total number count of workflows 
    def _workflowObjectCount(self):
        count_str_unfiltered = '//span[@id="objectsCounter"]' 
        
        count_str_filtered = self.util.getTextFromXpathString(count_str_unfiltered)
        endix = count_str_filtered.index(']')
        
        count = count_str_unfiltered[1:endix]
        
        return count

    @log_time
    def unmapObjectsWF(self, objectName):
        # TODO add search by title in the future; call _searchStringInTable()
        unmap_lk = '//div[@id="middle_column"]//div[@class="tier-2-info item-content content-open"]//a[@class="info-action unmap pull-right"]'
        total_count_label = '//div[@id="middle_column"]/section[@class="widget entities people_widget widget-active"]//span[@class="object_count"]'
        count = self.util.getTextFromXpathString(total_count_label)
        first_item = '//div[@id="middle_column"]//section[@class="widget objectives objects_widget widget-active"]//li[@class="tree-item object-top" and @data-index="0"]'

        self.util.hoverOver(first_item)
        self.util.clickOn(first_item)
        self.util.clickOn(unmap_lk)

    @log_time
    def unmapTasksWF(self, taskName):
        # TODO add search by title in the future; call _searchStringInTable()
        unmap_lk = '//div[@id="middle_column"]//div[@class="tier-2-info item-content content-open"]//a[@class="info-action unmap pull-right"]'
        total_count_label = '//div[@id="middle_column"]/section[@class="widget entities people_widget widget-active"]//span[@class="object_count"]'
        count = self.util.getTextFromXpathString(total_count_label)
        first_item = '//div[@id="middle_column"]//section[@class="widget objectives objects_widget widget-active"]//li[@class="tree-item object-top" and @data-index="0"]'
        
        self.util.hoverOver(first_item)
        self.util.clickOn(first_item)
        self.util.clickOn(unmap_lk)

    @log_time
    # Unmap first item in the list -- from the top
    def unmapPersonWF(self, personName):
        # TODO add search by title in the future; call _searchStringInTable()
        
        firstItem = '//div[@id="middle_column"]/section[@class="widget entities people_widget widget-active"]//span[@class="person-holder"]'
        unmap_lk = '//div[@id="middle_column"]//a[@class="info-action unmap pull-right"]'
        total_count_label = '//div[@id="middle_column"]/section[@class="widget entities people_widget widget-active"]//span[@class="object_count"]'
        count = self.util.getTextFromXpathString(total_count_label)

        self.util.hoverOver(firstItem)
        self.util.clickOn(firstItem)
        self.util.clickOn(unmap_lk)

    # Search for a specified text int the table, and return TRUE if found
    def _searchStringInTable(self, element, searchName, tableSize):
        
        for x in range[1:tableSize]:
            name = self.util.getTextFromXpathString(element)
            
            if name==searchName:
                return True
            else:
                continue

    @log_time
    # Unmap first item in the list -- from the top
    def deleteTaskGroupWF(self, groupName):        
        # TODO add search by title in the future
        count_xpath = '//div[@id="middle_column"]/section[@class="widget programs task_groups_widget widget-active"]//h2'
        title = '//div[@id="middle_column"]/section[@class="widget programs task_groups_widget widget-active"]//div[@class="tree-title-area"]'
        trash_icon = '//span[@class="counter removeTaskGroup"]/i'
        
        countBefore = self.util.getTextFromXpathString(count_xpath)
        # TODO Need to parse out the counter

        self.util.clickOn(trash_icon)
        time.sleep(1)

        if self.util.getTextFromXpathString(count_xpath) == countBefore-1:
            return True
        else:
            return False

    @log_time
    # Navigate inner panel on WorkFlow, e.g., Objects, Task Groups
    def navigateToMenuItemWF(self, fromWhatWorkflow, menuItem):
        workflow_menu  = '//li[@class="programs accordion-group workflow-group"]'
        workflow_items = '//li[@class="programs accordion-group workflow-group"]/ul[@class="sub-level"]/li[INDEX]//span'
        count_xpath = '//li[@class="programs accordion-group workflow-group"]//span[@class="item-count"]'

        self.util.clickOn(workflow_menu) # click on WorkFlow to expand it

        count = self.util.getTextFromXpathString(count_xpath)

        for x in count:
            label_text = self.util.getTextFromXpathString(workflow_items.replace("INDEX", x)) # click on WorkFlow to expand it
            
            if fromWhatWorkflow==label_text:
                self.util.clickOn(workflow_items.replace("INDEX", x))
                break
            else:
                continue

    @log_time
    # Return true if a named workflow exists, otherwise return false
    def doesWorkflowExist(self, wfName):
        workflow_menu  = '//li[@class="programs accordion-group workflow-group"]'
        workflow_items = '//li[@class="programs accordion-group workflow-group"]/ul[@class="sub-level"]/li[INDEX]//span'
        count_xpath = '//li[@class="programs accordion-group workflow-group"]//span[@class="item-count"]'

        self.util.clickOn(workflow_menu) # click on WorkFlow to expand it

        count = self.util.getTextFromXpathString(count_xpath)

        for x in count:
            label_text = self.util.getTextFromXpathString(workflow_items.replace("INDEX", x)) # click on WorkFlow to expand it
            
            if wfName==label_text:
                return True
            else:
                continue
        return False

    @log_time
    # Create a new work flow
    # If wfName is blank, it automatically create WF-auto + a timestamp, and return it
    def createWorkflow(self, wfName="", desc="", theFrequency="one_time", save=True):

        # TODO include more elements testing to support regression automation
        
        workflow_menu_lk  = '//li[@class="workflow accordion-group"]'
        workflow_items_lk = workflow_menu_lk + '/ul[@class="sub-level"]/li[INDEX]//span'
        wf_create_new_lk = workflow_menu_lk + '//li[@class="add-new"]'
        frequency_drdn = '//select[@id="frequency"]'
        
        title_txtbx = '//input[@name="title"]'
        owner_txtbx = '//input[@name="owners.0.email"]'
        owner_auto_row1 = '//li[@class="ui-menu-item"]/a[@href="javascript://"]/span'
        save_bt = '//div[@class="confirm-buttons"]/a[@data-toggle="modal-submit"]'
        cancel_bt = '//div[@class="deny-buttons"]/a[@data-dismiss="modal-reset"]'
               
        if (wfName == ""):
            wfName = self.getUniqueString("wf")
               
               
        self.openCreateNewObjectWindowFromLhn("Workflow")
        self.util.waitForElementToBePresent(title_txtbx, self.my_wait_time)
        self.util.inputTextIntoField(wfName, title_txtbx)
        #self.util.inputTextIntoField(desc, elem.object_iFrame)
        #self.util.waitForElementToBePresent(owner_auto_row1)
        #self.util.clickOn(owner_auto_row1)
        
        self.util.selectFromDropdownByValue(frequency_drdn, theFrequency)
        
        if save == True:
            self.util.clickOn(save_bt)
            time.sleep(10) # wait to avoid race condition       
            return wfName
        else:
            self.util.clickOn(cancel_bt)

    @log_time
    def expandWorkflowLHS(self):
        object_left_nav_section_object_link = elem.left_nav_expand_object_section_link.replace("OBJECT", "Workflow")
        self.assertTrue(self.util.waitForElementToBePresent(object_left_nav_section_object_link), "ERROR inside openCreateNewObjectWindowFromLhn():can't see the LHN link for workflow")
        self.util.clickOn(object_left_nav_section_object_link)


    #click on Create New (Workflow) link
    def selectCreateNewWF(self):
        wf_create_new_lk = '//li[@class="programs accordion-group workflow-group"]//li[@class="add-new"]'

    #click on Create New (Task) link 
    def pressCreateNewTaskLinkWF(self):
        expandTask_lhs = '//....'
        wf_create_new_lk = '//li[@class="programs accordion-group workflow-group"]//li[@class="add-new"]'      
      
        self.util.clickOn(expandTask_lhs)
        self.util.waitForElementToBeClickable(wf_create_new_lk, 5)
      
    @log_time
    def countWorkflowOnHLS(self):   
       wf_count = '//li[@class="programs accordion-group workflow-group"]/a/small/span'

       return  self.util.getTextFromXpathString(wf_count)


    @log_time
    # Select a workflow based the name and state {"Active", "Draft", "Inactive"}
    def selectAWorkflowWF(self, workflowName, uncheck=False, state="Draft"):
        workflow_items_lk = '//li[@class="workflow accordion-group"]//li[INDEX]//span'
        xpath_state = '//li[@class="workflow accordion-group"]//li[@class="filters"]//a[@data-value="' + state + '"]'
        
        if uncheck==True:
            # uncheck box if it is checked
            self.uncheckMyWorkBox()
            
        if "localhost" in config.url:
            time.sleep(15)
        else:
            time.sleep(50)

        self.util.waitForElementToBePresent(xpath_state)
        self.util.clickOn(xpath_state)
        endRange = self._countInsideParenthesis(self.util.getTextFromXpathString(xpath_state))
        
        if "localhost" in config.url:            
            time.sleep(15)
        else:
            time.sleep(50)
        
        # start from 2 because 1 is the state row: active/draft/inactive; adjusted by 2
        for index in range(2,endRange+2):           
            xpath =  str(workflow_items_lk).replace("INDEX", str(index))
            self.util.waitForElementToBePresent(xpath)
            time.sleep(1)
            mystr = self.util.getTextFromXpathString(xpath)
            #print "Troubleshooting => index: " + str(index) + ": " + mystr
            if mystr == workflowName:
                self.util.clickOn(xpath)
                return

    @log_time
    # Display the title of the currently active workflow, in case you want to know what is your current workflow name
    def theWorkflowTitle(self):
        title = '//div[@id="page-header"]/h1'

        
        return str(title)
                
    @log_time
    # Display the title of the currently active workflow, in case you want to know what is your current workflow name
    def aWorkflowTitle(self):
        title = '//div[@id="page-header"]/h1'
        
        return str(title)
                
    @log_time
    # Already in WorkFlow window, just want to select different menu item, e.g., Workflow Info, or Task Groups
    def selectInnerNavMenuItemWF(self, menuItem):
        ul_menu = '//ul[@class="nav internav  cms_controllers_inner_nav ui-sortable"]'
        li_WorkflowInfo = ul_menu + '/li/a[@href="#info_widget"]'
        li_People = ul_menu + '/li/a[@href="#person_widget"]'
        li_Setup = ul_menu + '/li/a[@href="#task_group_widget"]'
        li_History = ul_menu + '/li/a[@href="#history_widget"]'
        li_ActiveCycles = ul_menu + '/li/a[@href="#current_widget"]'
        li_ActivateWorkflow = ul_menu + '/li//button'

        if menuItem == "Workflow Info":
            self.util.clickOn(li_WorkflowInfo)
        elif menuItem == "People":
            self.util.clickOn(li_People)
        elif menuItem == "Setup":
            self.util.clickOn(li_Setup)
        elif menuItem == "History":
            self.util.clickOn(li_History)
        elif menuItem == "Active Cycles":
            self.util.clickOn(li_ActiveCycles)
        elif menuItem == "Activate Workflow":
            self.util.clickOn(li_ActivateWorkflow)
        time.sleep(1)

    @log_time
    # Edit a specified workflow
    def editWorkflowWF(self, workflowName, title="", owner="", save=True):
        edit_lk = '//div[@id="middle_column"]//a[@href="#editAssessmentStandAlone" and @title="Edit"]'
        my_title = '//div[@id="editAssessmentStandAlone"]//input[@name="title"]'
        my_owner = '//div[@id="editAssessmentStandAlone"]//input[@name="lead_email"]' 
        cancel_bt = '//div[@id="editAssessmentStandAlone"]//div[@class="deny-buttons"]/a'
        save_bt = '//a[@id="saveAssessment"]'

        self.navigateToMenuItemWF(workflowName, "Work Info")
        self.util.clickOn(edit_lk)
        self.util.waitForElementToBePresent(my_title, 8)

        self.util.inputTextIntoField(title, my_title)
        self.util.inputTextIntoField(owner, my_owner)

        # TODO add more other fields to support regression automation

        if save==True:
            self.util.clickOn(save_bt)
        else:
            self.util.clickOn(cancel_bt)

    @log_time
    # Clone a specified workflow
    def cloneWorkflowWF(self, workflowName, title="", owner="", save=True, copyTask=True, copyPeople=True, copyObjects=True, copyTaskGroup=True):
        self.navigateToMenuItemWF(workflowName, "Work Info")
        self._cloneWorkflow(title, owner, save, copyTask, copyPeople, copyObjects, copyTaskGroup)

    # Expand more link and click on Clone Workflow button
    def _cloneWorkflowWF(self, title="", owner="", save=True, copyTask=True, copyPeople=True, copyObjects=True, copyTaskGroup=True):
        more_lk = '//a[@class="dropdown-toggle info-edit"]'
        clone_workflow_bt = '//a[@href="#cloneWorkflow"]'
        cancel_bt = '//div[@id="cloneWorkflow"]//div[@class="deny-buttons"]/a'
        save_bt = '//a[@id="cloneWorkflowSave"]'

        myTitle = '//div[@id="cloneWorkflow"]//input[@name="title"]'
        myOwner = '//div[@id="cloneWorkflow"]//input[@name="lead_email"]'

        self.util.clickOn(more_lk)
        self.util.clickOn(clone_workflow_bt)
        self.util.waitForElementToBePresent(myTitle, 5)

        if (title != ""):
            self.util.inputTextIntoField(title, myTitle)

        if (owner != ""):
            self.util.inputTextIntoField(owner, myOwner)

        # by default, all checkboxes are checked
        if copyTask==False:
            self.util.clickOn('//div[@id="cloneWorkflow"]//label[1]/input[@type="checkbox"]')
        elif copyPeople==False:
            self.util.clickOn('//div[@id="cloneWorkflow"]//label[2]/input[@type="checkbox"]')
        elif copyObjects==False:
            self.util.clickOn('//div[@id="cloneWorkflow"]//label[3]/input[@type="checkbox"]')
        elif copyTaskGroup==False:
            self.util.clickOn('//div[@id="cloneWorkflow"]//label[4]/input[@type="checkbox"]')

        if save==False:
            self.util.clickOn(cancel_bt)
        else:
            self.util.clickOn(save_bt)

    @log_time
    # Prerequisite:  Add objects to workflow window is already up.  Add New Rule link is already there
    # Set add=False, to test the Cancel feature
    def addNewRule(self, object_type, relevantTo, searchItem, add=True, selectAll=False):
        select_all_drdn = '//select[@id="objects_type"]'
        add_new_rule_lk = '//a[@id="addFilterRule"]'
        relevant_to_drdn = '//div[@id="objectSelector"]//div[@class="indent-row"]//select'
        search_txtbx = '//div[@class="objective-selector"]//input[@class="input-large search-icon"]'
        search_bt = '//a[@id="objectReview"]'
        add_selected_bt = '//a[@id="addSelected"]'
        cancel_bt = '//div[@id="objectSelector"]//div[@class="deny-buttons"]'
        task_table = '//div[@class="tree-title-area"]/span/strong'

        self.util.selectFromDropdownByValue(select_all_drdn, object_type)
        self.util.clickOn(add_new_rule_lk)
        self.util.selectFromDropdownByValue(relevant_to_drdn, relevantTo)
        self.util.inputTextIntoField(searchItem, search_txtbx)

        self.util.clickOn(search_bt)

        if selectAll == True:
            self.util.clickOn(add_selected_bt)  # just click on the button
        else:
            count = self.util.countChildren(task_table) 
            idex = count.index(' ')
            count = count[0:idex]

            print "count: " + count

            for x in range(2, count):
                xpath = task_table + '/li[' + x + ']//div[@class="tree-title-area"]/i'
                title = self.util.getTextFromXpathString(xpath)
                print "title: " + title
                if title == searchItem:  # if found, click on the checkbox next to it
                    self.util.clickOn(task_table + '//input[@type="checkbox"]')  # check it
                    break  # get out

        if add==True:
            self.util.clickOn(add_selected_bt)
        else:
            self.util.clickOn(cancel_bt)

    @log_time
    # End the current cycle.  
    def endCycle(self):
        # select Current Cycle -> End Cycle
        end_cycle_bt = '//button[@class="btn end-cycle"]'

        self.selectInnerNavMenuItemWF("Current Cycle")
        self.util.waitForElementToBePresent(end_cycle_bt, 8)
        self.util.clickOn(end_cycle_bt)

    @log_time
    # Count the total of Objects in WF and return the number.
    def countObjectsWF(self, menuItem): 
        ul_menu = '//ul[@class="nav internav  cms_controllers_inner_nav ui-sortable"]'
        li_WorkflowInfo = ul_menu + '/li[1]//div'
        li_Objects = ul_menu + '/li[5]//div'
        li_Tasks = ul_menu + '/li[3]//div'
        li_People = ul_menu + '/li[2]//div'
        li_TaskGroups = ul_menu + '/li[4]//div'
        li_History = ul_menu + '/li[6]//div'
        li_CurrentCycle = ul_menu + '/li[7]//div'
        
        if menuItem == "Workflow Info":
            text = self.util.getTextFromXpathString(li_WorkflowInfo)
            count = self._count_helper(text)
        elif menuItem == "Objects":
            text = self.util.getTextFromXpathString(li_Objects)
            count = self._count_helper(text)
        elif menuItem == "Tasks":
            text = self.util.getTextFromXpathString(li_Tasks)
            count = self._count_helper(text)
        elif menuItem == "People":
            text = self.util.getTextFromXpathString(li_People)
            count = self._count_helper(text)
        elif menuItem == "Task Groups":
            text = self.util.getTextFromXpathString(li_TaskGroups)
            count = self._count_helper(text)
        elif menuItem == "History":
            text = self.util.getTextFromXpathString(li_History)
            count = self._count_helper(text)
        elif menuItem == "Current Cycle":
            text = self.util.getTextFromXpathString(li_CurrentCycle)
            count = self._count_helper(text)
            
        return count
        
    @log_time
    # lower-case please
    # Hide individual field or all
    # showOrHide tells whether you want to show or hide
    # list contains items to show or hide, "all" is a short hand for all
    def hideInWorkflowNewModal(self, hide=True, list=""):
        print "Start hideInWorkflowNewModal ..." 
          
        frequency_drdn = '//select[@id="frequency"]'
        frequency_drdn_hidden = '//select[@id="frequency"]/../../div[contains(@class, "hidden")]'
        hide_frequency_drdn = '//select[@id="frequency"]/../label/a'
        email_notify_chkbx = '//input[@type="checkbox" and @name="notify_on_change"]'  
        email_notify_chkbx_hidden = '//input[@type="checkbox" and @name="notify_on_change"]/../../div[contains(@class, "hidden")]' 
        hide_email_notify_chkbx = '//input[@type="checkbox" and @name="notify_on_change"]/../label/a'    
        first_taskgroup = '//input[@name="task_group_title"]'  
        first_taskgroup_hidden = '//input[@name="task_group_title"]/../../div[contains(@class, "hidden")]'
        hide_first_taskgroup = '//input[@name="task_group_title"]/../label/a'   
        custom_wf_email_msg = '//ul[contains(@id,"wf_modal_notify_message-wysihtml5-toolbar")]/parent::div/iFrame'
        custom_wf_email_msg_hidden = '//ul[contains(@id,"wf_modal_notify_message-wysihtml5-toolbar")]/parent::div/iFrame/../../../div[contains(@class, "span8 hidable hidden")]'
        hide_custom_wf_email_msg = '//ul[contains(@id,"wf_modal_notify_message-wysihtml5-toolbar")]/parent::div/iFrame/../../label/a'
        owner = '//input[@type="text" and @readonly="true"]'
        owner_hidden = '//input[@type="text" and @readonly="true"]/../../div[contains(@class, "hidden")]'
        hide_owner =   '//input[@type="text" and @readonly="true"]/../label/a'
          
          
        # if title exist that means modal is in view 
        self.util.waitForElementToBePresent(elem.object_title)
        time.sleep(3) # for all fields to show
          
        if hide==True:
            # regardless of current state, just want to hide all
            if "all" in list:
                # hide_all is visible
                if self.util.isElementPresent(elem.hide_all)==True:
                    self.util.clickOn(elem.hide_all)
                    time.sleep(10)
                    #verify that all non-mandatory fields are hidden
                    self.assertTrue(self.util.isElementPresent(elem.object_descriptionx_hidden))
                    self.assertTrue(self.util.isElementPresent(frequency_drdn_hidden))
                    self.assertTrue(self.util.isElementPresent(owner_hidden))
                    self.assertTrue(self.util.isElementPresent(email_notify_chkbx_hidden)) 
                    self.assertTrue(self.util.isElementPresent(first_taskgroup_hidden))
                    self.assertTrue(self.util.isElementPresent(custom_wf_email_msg_hidden)) 
                # show_all is visible    
                elif self.util.isElementPresent(elem.show_all)==True:
                    self.util.clickOn(elem.show_all) #even if one item is hidden, showAll displays
                    time.sleep(3)
                    self.util.waitForElementToBePresent(elem.hide_all)
                    self.util.clickOn(elem.hide_all)
                    time.sleep(8)
                    self.assertTrue(self.util.isElementPresent(elem.object_descriptionx_hidden))
                    self.assertTrue(self.util.isElementPresent(frequency_drdn_hidden))
                    self.assertTrue(self.util.isElementPresent(owner_hidden))
                    self.assertTrue(self.util.isElementPresent(email_notify_chkbx_hidden)) 
                    self.assertTrue(self.util.isElementPresent(first_taskgroup_hidden))
                    self.assertTrue(self.util.isElementPresent(custom_wf_email_msg_hidden)) 
                
                # take snapshot
                self.getScreenshot("screen_wf_hide_all")
            # hide individual item(s)
            else:
                if 'description' in list:
                    self.assertFalse(self.util.isElementPresent(elem.object_descriptionx_hidden))
                    self.util.clickOn(elem.hide_object_descriptionx)
                    time.sleep(3)
                    self.assertTrue(self.util.isElementPresent(elem.object_descriptionx_hidden))
                if 'frequency' in list:
                    self.assertFalse(self.util.isElementPresent(frequency_drdn_hidden))
                    self.util.clickOn(hide_frequency_drdn)
                    time.sleep(3)
                    self.assertTrue(self.util.isElementPresent(frequency_drdn_hidden))
                if 'owner' in list:
                    self.assertFalse(self.util.isElementPresent(owner_hidden))
                    self.util.clickOn(hide_owner)
                    self.assertTrue(self.util.isElementPresent(owner_hidden))
                    time.sleep(3)   
                if 'email' in list:
                    self.assertFalse(self.util.isElementPresent(email_notify_chkbx_hidden))
                    self.util.clickOn(hide_email_notify_chkbx)
                    time.sleep(3)
                    self.assertTrue(self.util.isElementPresent(email_notify_chkbx_hidden)) 
                if 'first_task_group' in list:
                    self.assertFalse(self.util.isElementPresent(first_taskgroup_hidden))
                    self.util.clickOn(hide_first_taskgroup)
                    time.sleep(3)
                    self.assertTrue(self.util.isElementPresent(first_taskgroup_hidden)) 
                if 'custom_email_message' in list:
                    self.assertFalse(self.util.isElementPresent(custom_wf_email_msg_hidden))
                    self.util.clickOn(hide_custom_wf_email_msg)
                    time.sleep(3)
                    self.assertTrue(self.util.isElementPresent(custom_wf_email_msg_hidden))               

        else:
            # cannot unhide individual item so if show_all button exist click on it
            if self.util.isElementPresent(elem.show_all)==True:
                self.util.clickOn(elem.show_all)        
        
        
        
        
        
        
        
        
    # Private function.  Filter out extra text and left, right parenthesis and return the content in between which is count
    def _count_helper(self, text):
        start = text.index("(") + 1
        end = text.index(")")
        text = text[start:end]
        return text
