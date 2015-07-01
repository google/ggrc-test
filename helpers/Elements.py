'''
Created on Jun 18, 2013

@author: diana.tzinov
'''


class Elements(object):

        script_error_css = '[class="alert alert-error"]'
        script_error_xpath = '//div[@class="alert alert-error"]'
        modal_window = '//div[@class="modal-body"]'
        audit_area_plus_audit_link = '//a[contains(@data-object-singular,"Audit")][contains(@class,"section-create")]'
        audit_area_create_audit_link = '//span[contains(@class,"section-expander")]//a[@data-object-singular="Audit"]'
        audit_area_by_title = '//li[@data-object-type="audit"][descendant::div[@class="tree-title-area"][contains(., "AUDIT_TITLE")]]'
        audit_edit = '//ancestor::li[@data-object-type="audit"]//i[@class="grcicon-edit"]/parent::a'
        audit_area_created_audit_open_link = '//li[@data-object-type="audit"]//a//div[@class="tree-title-area"][contains(.,"AUDIT_TITLE")]/parent::div/parent::div/parent::div/parent::a'

        audit_modal_autogenerate_checkbox = '//input[@name="auto_generate"]'
        audit_modal_start_date_input = '//input[@name="start_date"]'
        audit_modal_end_date_input = '//input[@name="end_date"]'
        audit_modal_report_start_date_input = '//input[@name="report_start_date"]'
        audit_modal_report_end_date_input = '//input[@name="report_end_date"]'
        audit_modal_firm_input_field = '//input[@name="audit_firm.email"]'
        audit_modal_description_text = 'This is an automated test run of the Audit workflow feature set.'
        audit_modal_firm_text = 'Reciprocity'
        audit_modal_audit_lead_input_field = '//input[@name="contact.email"]'
        audit_modal_audit_lead_value = 'testrecip@gmail.com'
        audit_pbc_request = '//li[@data-object-type="request"][contains(.,"TITLE")]'
        audit_pbc_request_expanded = audit_pbc_request + '//div[@class="show-description"]'
        audit_pbc_request_modal_type_select = modal_window + '//select[@name="request_type"]'
        audit_pbc_request_modal_type_select_selected_option = modal_window + '//select[@name="request_type"]/option[@selected]'
        audit_pbc_request_type_select = audit_pbc_request + '//select[@name="request_type"]'
        audit_pbc_request_type_select_selected_option = audit_pbc_request +'//select[@name="request_type"]/option[@selected]'
        audit_pbc_request_expand_collapse_button =audit_pbc_request +'//div[@class="item-main"]//a[contains(@class,"openclose")]'
        audit_pbc_request_expand_collapse_button2 =audit_pbc_request +'/div[@class="item-main"]//a[contains(@class,"openclose")]'
        audit_pbc_request_state_button = audit_pbc_request + '//div[contains(@class, "request-control")]//button[@data-name="status"]'
        audit_pbc_request_response = audit_pbc_request +'//li[contains(@class,"responses-list")]//a'
        audit_pbc_request_response2 = audit_pbc_request + '//ul[contains(@class,"responses-list")]/li[contains(.,"RESPONSE")]' 
        audit_pbc_request_response_create = '//li[@data-object-type="request"][contains(.,"TITLE")]//a[@class="section-create"][@data-object-plural="responses"]'
        
        #audit_pbc_request_response_expand_collapse_link = audit_pbc_request +'//li[@data-object-type="documentation_response"]//a[contains(@class,"openclose")]'
        audit_pbc_request_response_expand_collapse_link = audit_pbc_request +'//ul[contains(@class,"responses-list")]/li[contains(., "RESPONSE")]//a[contains(@class,"openclose")]'

        audit_pbc_request_response_add_object_link = audit_pbc_request +'//li[contains(@class,"responses-list")]//a[@data-join-mapping="business_objects"]'

        audit_pbc_request_expanded_content_response_email_inputfield = audit_pbc_request_response + '//input[@data-lookup="Person"]'
        audit_pbc_request_expanded_content_add_response_button= audit_pbc_request + '//li[@class="tree-item tree-item-add tree-footer"]//div[contains(@class, "expandable")]/a[contains(text(),"PBC Response")]'
        audit_pbc_request_expanded_content_create_response_button= audit_pbc_request + '//li[@class="tree-item tree-item-add tree-footer"]//span/a'
        #audit_request_expanded_content = '//li[@class="tree-item programs request-list cms_controllers_tree_view_node item-open"]'
        audit_pbc_request_expanded_content_edit_link = '//a[@class="utility-link"][@data-object-singular="Request"]'
        audit_pbc_request_expanded_response_edit_link = '//a[@class="utility-link"][@data-object-singular="Response"]'
        audit_pbc_request_expanded_response_edit_link2 = audit_pbc_request_response2 + audit_pbc_request_expanded_response_edit_link
        audit_pbc_request_response_mapped_org_group_object_withrecipprocity_dev_team = '//div/h6[contains(text(),"Mapped Objects")]/parent::div//li[@data-object-id="3"]'

        add_widget_plus_sign = '//a[@href="#dropdown-widgets"]/i'
        audit_pbc_request_response_upload_evidence_link =audit_pbc_request+ ' //li[contains(@class,"responses-list")]//a[@title="Upload Evidence"]'
        audit_pb_request_response_evidence_folder_link = audit_pbc_request+'//a[contains(@href,"folderview")]'
        audit_pbc_request_response_add_object_link_within_response = audit_pbc_request +'//a[@data-join-mapping="business_objects"]'
        audit_pbc_request_response_add_person_within_response = audit_pbc_request +'//a[@data-join-mapping="people"]'
        audit_pbc_request_response_participant_email = '//span[@class="person-holder"]//span[contains(.,"EMAIL")]'
        audit_pbc_request_response_add_meeting = audit_pbc_request +'//a[@class="section-add"][contains(text(),"Meeting")]'
        audit_pbc_request_response_create_meeting = audit_pbc_request +'//a[@data-object-singular="Meeting"]'
        audit_pbc_request_response_interview_open_close = '//li[@data-object-type="interview_response"]//div[@data-model="true"]//a[contains(@class,"openclose")]'
        audit_pbc_request_response_population_sample_open_close = '//li[@data-object-type="population_sample_response"]//div[@data-model="true"]//a[contains(@class,"openclose")]'
        
        datepicker_calendar = '//div[@id="ui-datepicker-div"]//table[@class="ui-datepicker-calendar"]'
        datepicker_month_dropdown = '//select[@class="ui-datepicker-month"]'
        datepicker_year_dropdown = '//select[@class="ui-datepicker-year"]'
        logo = '//div[contains(@class,"logo")]/a'
        login_button = '//p/a[@href="/dashboard"]' 
        gapi_app_permission_form = '//div[@id="third_party_info_container"]'
        gapi_app_permission_authorize_button = gapi_app_permission_form + '//form[@id="connect-approve"]//button[@id="submit_approve_access"]'
        gapi_modal = '//div[contains(@class, "ggrc_controllers_gapi_modal")]'
        gapi_modal_authorize_button = gapi_modal + '//a[contains(@class, "btn")][@data-toggle="gapi"]'

        gmail_userid_textfield = '//input[@id="Email"]'
        gmail_password_textfield = '//input[@id="Passwd"]'
        gmail_submit_credentials_button = '//input[@type="submit"]'

        g_accounts_login_prompt = '//form[contains(@action, "appengine.google")]'
        g_accounts_remember_box = '//input[@id="persist_checkbox"]'
        g_accounts_allow = '//form//input[@name="submit_true"]'
        g_accounts_disallow = '//form//input[@name="submit_false"]'

        chrome_login_prompt = '//form[contains(@action, "ChromeLoginPrompt")]'
        chrome_login_skip_button = chrome_login_prompt + """//input[@onclick="setFormAction('no')"]"""

        first_link_within = '//a'
        flash_box = '//div[@class="flash"]'
        flash_box_type = flash_box + '//div[contains(@class, "alert-TYPE")]'
        flash_box_type_dismiss = flash_box_type + '//a[@class="close"]'
        flash_types = ['success', 'error', 'notice']

        google_permission_prompt = '//input[@id="approve_button"]'
        google_permission_yes = '//input[@id="approve_button" and @name="submit_true"]'
        google_permission_remember = '//input[@id="persist_checkbox"]'

        google_calendar_meeting_time = '//div[@class="ui-sch-schmedit"]'
        google_meeting_title = '//div[@class="ui-sch ep-title"]/div[@class="ui-sch-schmedit"]'
        #dashboard_title= '//h1[@class="entities"]'
        dashboard_title= '#page-header.entities'
        
        left_nav_search_input_textfield= '//input[contains(@class,"widgetsearch")]'
        
        left_nav_governance_controls_numbers = '//li[contains(@class,"governance")][1]/a//span[@class="item-count"]'
        left_nav_governance_controls_numbers_not_loaded = '//li[contains(@class,"governance")][1]/a//span[contains(.,"...")]'
        left_nav_governance_contracts_numbers = '//li[contains(@class,"governance")][2]/a//span[@class="item-count"]'
        left_nav_governance_contracts_numbers_not_loaded = '//li[contains(@class,"governance")][2]/a//span[contains(.,"...")]'
        
        left_nav_governance_policies_numbers = '//li[contains(@class,"governance")][3]/a//span[@class="item-count"]'
        left_nav_governance_policies_numbers_not_loaded= '//li[contains(@class,"governance")][3]/a//span[contains(.,"...")]'
        left_nav_governance_regulations_numbers = '//li[contains(@class,"governance")][4]/a//span[@class="item-count"]'
        left_nav_governance_regulations_numbers_not_loaded = '//li[contains(@class,"governance")][4]/a//span[contains(.,"...")]'
        
        left_nav_risk_assessment_link = '//a[@class="risk" and @data-object-singular="RiskAssessment"]'
        left_nav_market_link = '//a[@class="business oneline" and @data-object-singular="Market"]'
        left_nav_data_asset_link = '//a[@class="business oneline" and @data-object-singular="DataAsset"]'
        left_nav_org_group_link = '//a[@class="entities oneline" and @data-object-singular="OrgGroup"]'
        left_nav_expand_object_section_link = '//ul[@class="top-level"]//li[contains(@data-model-name,"OBJECT")]/a'
        left_nav_expand_status = left_nav_expand_object_section_link + '[contains(@class, "active")]'
        left_nav_expand_object_section_link_one_result_after_search = '//ul[@class="top-level"]//li[contains(@data-model-name,"OBJECT")]/a//span[@class="item-count"][not(contains(.,"(0)"))]'
        left_nav_sections_loaded = '//ul[@class="top-level"]//li[contains(@data-model-name,"Control")]/a//span[@class="item-count"][not(contains(.,"()"))]'  # for confirming that LHN itmes are loaded -- have a value the parens
        left_nav_object_section_add_button = "li .add-new.oneline > a[data-object-singular=OBJECT]"
        # ToDo: @ambarish: Changed the string 'Contract' to OBJECT in the above CSS. Might need to edit it later
        left_nav_last_created_object_link = '//ul[@class="top-level"]//li[contains(@data-model-name,"SECTION")]//li[contains(.,"OBJECT_TITLE")]/a'
        #left_nav_first_object_link_in_the_section = '//ul[@class="top-level"]//li[contains(@data-model-name,"SECTION")]/div/ul[contains(@class, "sub-level")]/li[@data-model="true"]/a[contains(@class, "show-extended")]/../../li[1]'
        left_nav_first_object_link_in_the_section = '//li[@class="governance"][1]//div[@class="lhs-main-title"]/span[1]'
        left_nav_first_object_link_in_the_section_object_name = '//ul[@class="top-level"]//li[@data-model-name="SECTION"]//li[1]/a//span[@class="lhs-item"]'
       
        left_nav_objects_candidate_for_deletion = '//ul[@class="top-level"]//li[contains(@data-model-name,"SECTION")]//li[1]/a//span[contains(.,"Auto")]/parent::div/parent::div/parent::a'
       
        inner_nav_object_link = '//div[@class="inner-nav"]//div[@class="object-nav"]//a[contains(@href,"OBJECT")][contains(.,")")][contains(.,"(")]'
        inner_nav_section = '//div[@class="inner-nav"]'
        inner_nav_object_with_one_mapped_object = '//div[@class="inner-nav"]//div[@class="object-nav"]//a[contains(@href,"OBJECT")]/div[contains(.,"1")]'
        
        #map_to_this_object_link = '//a[@class="primary map-to-page-object"]'
        map_to_this_object_link = '//div[@id="extended-info"][contains(concat(" ", normalize-space(@class), " "), " in ")]//a[contains(@class, "map-to-page-object")]'
        mapped_object_person = '//section[@id="person_widget"]//div[@class="select"]//div[@class="row-fluid"]/div[1]/div[1]'
        mapped_object = '//section[@id="OBJECT_widget"]//div[@class="select"]//div[@class="row-fluid"]/div[@class="span4"]/div[1]'
        mapped_object_area_section_add_link = '//section[contains(@id,"OBJECT")]//li[@data-object-id=ID]//a[@class="section-add"]'
        # "or" clause because a person lacking a name will have the email text fall into the span.person-holder element instead
        mapped_person_program_email = '//section[contains(@id,"person")]//li[contains(@class, "person")]//span[contains(@class, "person-holder") or contains(@class, "email")][contains(., "EMAIL")]'
        # NOTE: Something magical happens that keeps this selector from working unless you copy the string "Mapped" directly from the DOM and use it.
        mapped_person_program_mapped_label = '/../../../..//*[@class="role"][contains(text(),"Mapped")]'
        
        mapping_modal_window = '//div[@class="modal-filter"]'
        mapping_modal_window_map_button = '//div[@class="confirm-buttons"]//a'
        #mapping_modal_window_map_button = '//a[contains(@class,"map-button")]'
        mapping_modal_selector_list_first_object = '//div[contains(@class, "selector-list")]//li[1]'
        mapping_modal_selector_list_first_object_link = '//div[contains(@class, "selector-list")]//li[1]//div[@class="tree-title-area"]/parent::div'
        mapping_modal_selector_first_nonself_object_link = '//div[contains(@class, "selector-list")]//li[contains(@class, "tree-item")][not(@data-id="OBJECTID")][1]//div[@class="tree-title-area"]/parent::div'
        mapping_modal_selector_list_first_object_link_with_specific_title = '//div[contains(@class, "selector-list")]//li[1]//div[@class="tree-title-area"][contains(., "TITLE")]/parent::div'
        
        mapping_modal_selector_list_first_object_email = mapping_modal_selector_list_first_object + '//span[@class="url-link"]'
        mapping_modal_input_textfiled = '//div[@class="modal-content"]//input'
        mapping_modal_add_button = '//a[contains(@class,"btn-add")]'
        mapping_modal_top_filter_selector_dropdown = '//select[contains(@class,"input-block-level")]'
        mapping_modal_top_filter_selector_dropdown_reciprocity_dev_team_option = '//div[contains(@class, "selector-list")]//li[@data-id="3"]//span'
        mapping_modal_search_reset = '//a[contains(@class,"search-reset")]'
        
        modal_window_show_hidden_fields_link = '//a[@class="show-hidden-fields"]'
        modal_window_delete_button = '//a[contains(@data-toggle, "deleteform")]'
        modal_window_confirm_delete_button = '//div[@class="confirm-buttons"]/a[@data-toggle="delete"]'
        modal_window_hidden_fields_area = '//div[@class="hidden-fields-area"]'
        modal_window_save_button = '//div[@class="confirm-buttons"]//a[contains(text(),"Save & Close")]'
        modal_window_save_add_another_button = '//div[@class="confirm-buttons"]//a[contains(text(),"Save & Add Another")]'
        modal_window_X_button = '//a[@class="btn btn-danger btn-mini pull-right"]/i'
        modal_window_cancel_button = '//div[@class="deny-buttons"]//a[contains(text(),"Cancel")]'
        modal_window_private_checkbox = '//input[@name="private"]'

        my_work_checkbox_selected = '//a[@data-value="my_work" and @class="active"]'
        everyone_work_checkbox_selected = '//a[@data-value="all" and @class="active"]'
        my_work_checkbox = '//a[@data-value="my_work"]'
        everyone_work_checkbox = '//a[@data-value="all"]'
        my_work_parent = '//input[@class="my-work"]/..'


        meeting_title_input_textfield = '//div[@class="modal-body"]//input[@name="title"]'
        meeting_date = '//div[@class="modal-body"]//input[@name="start_at.date"]'
        meeting_start_time_dropdown = '//div[@class="modal-body"]//select[@name="start_at.time"]'
        meeting_end_time_dropdown =   '//div[@class="modal-body"]//select[@name="end_at.time"]'
        meeting_participant_select = '//select[@model="Person"]'
        meeting_participant_select_first = '//select[@model="Person"]/option[1]'
        meeting_participant_select_second = '//select[@model="Person"]/option[2]'
        meeting_edit_link = '//a[@class="utility-link"][@data-object-singular="Meeting"]'
        meeting_gcal_link = '//a[contains(@href,"/calendar/event")]'
        meeting_expnad_link = '//li[@data-object-type="meeting"]//a[contains(@class,"openclose")]'

        object_detail_page_edit_link = '//section[contains(@id,"info_widget")]//a[contains(@title,"Edit")]'
        object_detail_page_info_section = '//section[contains(@id,"info_widget")]'
        #object_info_page_edit_link = '//div[@id="middle_column"]//a[@title="Edit "]'
        #object_title = '//input[@name="title"]'
        object_description = '//div[@class="modal-body"]/form/div[2]//div[@class="wysiwyg-area ui-resizable"]/iframe'
        #response_title = '//ul[contains(@id,"FRAME_NAME")]/parent::div/iFrame'
        response_title = '//ul[contains(@id,"description")]/parent::div/iFrame'
        response_assignee = '//input[@name="contact.email"]'
        object_title_value = '//div[@class="modal-body"]/form//input[@name="title"]/@value'
        object_iFrame = '//ul[contains(@id,"FRAME_NAME")]/parent::div/iFrame'
        object_owner = '//input[@data-id="owner_txtbx"]'
        object_url = '//div[@class="modal-body"]//div[@class="row-fluid"]//input[@name="url"]'
        object_code = '//input[@name="slug"]'
        object_organization = '//div[@class="hidden-fields-area"]//input[@name="organization"]'
        object_scope = '//div[@class="hidden-fields-area"]//input[@name="scope"]'
        object_dropdown = '//select[@name="NAME"]'
        object_dropdown_selected_option = '//select[@name="NAME"]/option[@selected]'

        data_object_element = '//li[@data-object-type="DATA_OBJECT"]'
        data_object_element_with_index = '//li[@data-object-type="DATA_OBJECT"][INDEX]'
        

        objective_elemet_in_the_inner_tree = '//div[@class="inner-tree"]//li[@data-object-type="objective"]'
        objective_elemet_in_the_inner_tree_with_index = '//div[@class="inner-tree"]//li[@data-object-type="objective"][INDEX]'
        objective_id = '//li[@data-object-type="objective"][INDEX]'
        
        section_widget = '//section[contains(@id,"SECTION")]'
        section_widget_join_object_link = '//section[contains(@class,"content")]//a[contains(@data-join-option-type,"OBJECT")]'
        section_widget_expanded_join_link1 = '//section[contains(@id,"OBJECT_widget")]//a[@class="section-add"]'
        section_widget_expanded_join_link2 = '//section[contains(@id,"widget")]//span[contains(@class,"section-expander")]//a[contains(@data-join-option-type,"OBJECT")]'
        section_widget_expanded_sectionObject_link3 = '//section[contains(@id,"widget")]//span[contains(@class,"section-expander")]//a[contains(@data-object-singular,"OBJECT")]'
        section_widget_tree = '//section[contains(@id, "OBJECT_widget")]//ul[contains(@class, "tree-structure")]'
        list_loaded_suffix = '[contains(@class, "list-loaded")]'
        map_modal_loaded = '//body/div[contains(@class, "modal-selector")][contains(@class, "list-loaded")]'
        section_active = '//div[contains(@class, "object-nav")]//ul[contains(@class, "inner_nav")]/li[contains(@class, "active")]/a[contains(@href, "SECTION")]'
        section_add_link = '//a[@class="section-add"]'
        section_create_link = '//a[@class="section-create"]'
        sections_area_first_section = '//li[@data-object-type="section"][1]//div[@class="tree-title-area"]/span'
        section_area_add_object_link = '//div[contains(@class,"section-expandable")]//a[contains(text(),"+ Object")][contains(@class,"sticky")]'
        section_area_add_objective_link = '//div[contains(@class,"section-expandable")]//a[contains(text(),"+ Objective")]'
        search_inputfield = '//input[@can-value="search_text"]'
        section_pol_reg_std = '//input[@data-lookup="Policy,Regulation,Standard"]'


        autocomplete_list_first_element = '//ul[contains(concat(" ", normalize-space(@class), " "), " ui-autocomplete ")]/li[contains(@class, "ui-menu-item")]'
        autocomplete_list_element_with_text = '//ul[contains(concat(" ", normalize-space(@class), " "), " ui-autocomplete ")]/li[contains(@class, "ui-menu-item")]/a/span[contains(text(), "TEXT")]/..'
        autocomplete_list_element_with_text2 =  '//ul[contains(@class, "ui-autocomplete")]/li[contains(@class, "ui-menu-item")]/a[contains(., "TEXT")]'

        theLongTextDescription1 = """
Section 1 of this regulation will have several objectives extracted from it. When creating the objectives we will want to make sure that:
* the Text of the section text is auto copied to the Objective description
* multiple objectives per sesction is easily supported and working
* creation of a control under the section works as well

Evidence of this should be provided as Screenshot        
        """
        theShortTextDescription = 'Section 1 of this regulation will have several objectives extracted from it.'
        theShortDescriptionElement = '//div[@class="tree-description short"]'       
        select_file_dialog_window = '//div[@class="picker-frame picker-dialog-frame"]'
        select_file_iframe = '//iFrame[contains(@class,"picker-frame picker-dialog-frame")]'
        #select_file_button = '//div[contains(@id,"select-files-button")]//input[@type="file"]'
        select_file_button = '//input[@type="file"]'
        upload_file_button ='//div[@id="picker:ap:0"]'
        title_duplicate_warning = "//label[@class='help-inline warning']"
        #new_person_name = '//input[@id="person_name"]'
        new_person_name = "#person_name"
        #new_person_email = '//input[@id="person_email"]'
        new_person_email = '#person_email'
        new_person_company = '//input[@id="person_company"]'       
        section_add_link_from_inner_nav = '//a[@href="javascript://" and @class="section-add"]'
        section_create_link_from_inner_nav = '//a[@href="javascript://" and @class="section-create"]'
        
        first_item_section_link_from_nav = '//li[@class="tree-item governance cms_controllers_tree_view_node"]//div[@class="tree-title-area"]'
        map_object_to_section_from_nav = '//a[@data-original-title="Map Object to this Section"]'
        dropdown_from_map_object_window_OBJECT = '//select[@class="input-block-level option-type-selector"]//option[@value="OBJECT"]'      
        list_of_items_to_select_from = '//ul[@class="new-tree"]//div[@class="tree-title-area"]'
        map_button_on_map_object_windown = '//div[@class="confirm-buttons"]/a'
        unmap_button_from_2nd_level_regulation = '//div[@id="middle_column"]//a[@data-object-singular="Regulation"]/../a[@data-toggle="unmap"]'
        unmap_button_from_3rd_level_object = '//li[@class="tree-item cms_controllers_tree_view_node item-open" and @data-object-type="person"]//i[@class="grcicon-remove"]'
        edit_section_link_from_inner_mapping = '//section[@id="regulation_widget"]//a[@title="Edit Section"]' #program->regulation->section
        item_from_list_widget = '//div[@class="tree-title-area"]/span'
        search_box_in_map_object = '//input[@id="search"]'
        expand_collapse_object_map_entry = '//div[@class="item-main"]//div[@class="item-data"]'
        first_item_from_a_section = '//ul[@class="top-level"]//li[contains(@data-model-name,"OBJECT")]/a/../div/ul/li[1]//span[@class="lhs-item"]'
        expand_collapse_widget_first_row = '//li[1]//div[@class="tree-title-area"]'       
        section_add_link_from_inner_nav = '//a[@href="javascript://" and @class="section-add"]'
        section_create_link_from_inner_nav = '//a[@href="javascript://" and @class="section-create"]'
        first_item_section_link_from_nav = '//li[@class="tree-item governance cms_controllers_tree_view_node"]//div[@class="tree-title-area"]'
        map_object_to_section_from_nav = '//a[@data-original-title="Map Object to this Section"]'
        dropdown_from_map_object_window_OBJECT = '//select[@class="input-block-level option-type-selector"]//option[@value="OBJECT"]'      
        list_of_items_to_select_from = '//ul[@class="new-tree"]//div[@class="tree-title-area"]'
        map_button_on_map_object_windown = '//div[@class="confirm-buttons"]/a'
        unmap_button_from_2nd_level_regulation = '//div[@id="middle_column"]//a[@data-object-singular="Regulation"]/../a[@data-toggle="unmap"]'
        unmap_button_from_3rd_level_object = '//li[@class="tree-item cms_controllers_tree_view_node item-open" and @data-object-type="person"]//i[@class="grcicon-remove"]'
        edit_section_link_from_inner_mapping = '//section[@id="regulation_widget"]//a[@title="Edit Section"]' #program->regulation->section
        item_from_list_widget = '//div[@class="tree-title-area"]/span'
        search_box_in_map_object = '//input[@id="search"]'
        expand_collapse_object_map_entry = '//div[@class="item-main"]//div[@class="item-data"]'
        first_item_from_a_section = '//ul[@class="top-level"]//li[contains(@data-model-name,"OBJECT")]/a/../div/ul/li[1]//span[@class="lhs-item"]'
        unmap_successful_txt ='//div[@class="alert alert-success"]/span'
        unmap_successful_x_bt ='//div[@class="alert alert-success"]/a[@data-dismiss="alert"]'
        audit_program_dd = '[data-id=program_dd]'
        
        # elements on new object creation modal
        hide_all = '//a[@id="formHide"]'
        hide_all_id = 'formHide' # by id
        show_all = '//a[@id="formRestore"]'
        show_all_id = 'formRestore' # by id, not by xpath
        reference_url = '//input[@id="reference_url"]'
        new_program_reference_url_hidden = '//input[@id="reference_url"]/../../div[contains(@class, "hidden")]'
        hide_reference_url = '//input[@id="reference_url"]/../label/a'
        object_url = '//input[@name="url"]'       
        hide_object_url = '//input[@name="url"]/../label/a'
        new_program_url_hidden = '//input[@name="url"]/../../div[contains(@class, "hidden")]'
        owner = '//input[@name="owners.0.email"]'
        hide_owner = '//input[@name="owners.0.email"]/../label/a'     
        new_program_owner = '//input[@placeholder="Enter email address" and @readonly="true"]'
        hide_new_program_owner = '//input[@placeholder="Enter email address" and @readonly="true"]/../../label/a'
        new_program_owner_hidden = '//input[@placeholder="Enter email address" and @readonly="true"]/../../../div[contains(@class, "hidden")]'
        contact = '//input[@name="contact.email"]'
        hide_contact = '//input[@name="contact.email"]/../label/a'
        new_program_contact_hidden = '//input[@name="contact.email"]/../../div[contains(@class, "hidden")]'
        new_stop_date = '//input[@name="end_date"]'
        hide_new_stop_date = '//input[@name="end_date"]/../label/a'
        new_program_stop_date_hidden = '//input[@name="slug"]/../../div[contains(@class, "hidden")]/input[@name="end_date"]'
        new_effective_date = '//input[@name="start_date"]'
        new_program_effective_date_hidden = '//input[@name="slug"]/../../div[contains(@class, "hidden")]/input[@name="start_date"]'
        hide_new_effective_date = '//input[@name="start_date"]/../label/a'
        new_state_dropdown = '//select[@name="status"]'
        new_program_state_dropdown_hidden = '//select[@name="status"]/../../div[contains(@class, "hidden")]'
        hide_new_state_dropdown = '//select[@name="status"]/../label/a'
        new_note = '//ul[contains(@id,"notes")]/parent::div/iFrame'  
        hide_new_note = '//ul[contains(@id,"notes")]/parent::div/iFrame/../../label/a'
        new_note_hidden = '[data-id="note_hidden"][class*="hidden"]'
        new_code = '//input[@name="slug"]'
        hide_new_code = '//input[@name="slug"]/../label/a'
        new_program_code_hidden = '//input[@name="slug"]/../../div[contains(@class, "hidden")]/input[@placeholder="PROGRAM-XXX"]'
        object_descriptionx = '//ul[contains(@id,"description")]/parent::div/iFrame'    
        object_descriptionx_hidden = '//ul[contains(@id,"description")]/parent::div/iFrame/../../../div[contains(@class, "span8 hidable hidden")]'
        object_new_prgm_desc_hidden = '//ul[contains(@id,"description")]/parent::div/iFrame/../../../div[contains(@class, "span6 hidable hidden")]'
        hide_object_descriptionx = '//ul[contains(@id,"description")]/parent::div/iFrame/../../label/a'
        new_private_program = '//input[@name="private"]'
        hide_new_private_program = '//input[@name="private"]/../../label/a'
        new_private_program_hidden = '//input[@name="private"]/../../../div[contains(@class, "span6 hidable hidden")]'
        private_program_chkbx = '//input[contains(@type, "checkbox") and (@value="private")]'
        
        # *** Starting from here down are Id(s) created for automation, added to mustache file by automation coder
        title_modal = '//input[@data-id="title_txtbx"]'
        title_modal_audit_edit_window_css = '//input[@data-id="title_2_txtbx"]'
        owner_modal = '//input[@data-id="owner_txtbx"]'
        contact_modal = '//input[@data-id="contact_txtbx"]'
        url_modal = '//input[@data-id="url_txtbx"]'
        reference_url_modal = '//input[@data-id="reference_url_txtbx"]'        
        code_modal = '//input[@data-id="code_txtbx"]'
        effective_date_modal = '//input[@data-id="effective_date_txtbx"]' 
        stop_date_modal = '//input[@data-id="stop_date_txtbx"]'
        state_modal = '//select[@data-id="state_dd"]' 
        description_xpath_modal = '//ul[contains(@id,"description")]/parent::div/iFrame'
        note_xpath_modal = '//textarea[contains(@data-id,"note_txtbx")]/parent::div/iFrame'
        kind_type_modal = '//select[@data-id="kind_type_dd"]'

        hidden_owner_modal = '//div[@data-id="owner_hidden" and contains(@class,"hidden")]'
        hidden_contact_modal = '//input[@data-id="contact_txtbx"]/../../div[contains(@class, "hidden")]'
        hidden_url_modal = '//div[@data-id="url_hidden" and contains(@class,"hidden")]'
        hidden_reference_url_modal = '//div[@data-id="reference_url_hidden" and contains(@class,"hidden")]'      
        hidden_code_modal = '//div[@data-id="code_hidden" and contains(@class, "hidden")]'
        hidden_effective_date_modal = '//div[@data-id="effective_date_hidden" and contains(@class,"hidden")]'
        hidden_stop_date_modal = '//div[@data-id="stop_date_hidden" and contains(@class,"hidden")]'
        hidden_state_modal = '//div[@data-id="state_hidden" and contains(@class,"hidden")]'  
        hidden_note_modal = '//div[@data-id="note_hidden" and contains(@class, "hidden")]'
        hidden_description_modal = '//div[@data-id="description_hidden" and contains(@class, "hidden")]' 
        hidden_kind_type_modal = '//div[@data-id="kind_type_hidden" and contains(@class,"hidden")]'
        hidden_network_zone_modal = '//div[@data-id="network_zone_hidden" and contains(@class,"hidden")]'
        hidden_private_program_modal = '//div[@data-id="privacy_hidden" and contains(@class,"hidden")]'

        # CCS is better than Xpath because it does not require the element type, e.g., div, li, span
        hidden_kind_nature_modal_css = '[data-id=kind_nature_hidden][class*="hidden"]'
        hidden_fraud_related_modal_css = '[data-id=fraud_related_hidden][class*="hidden"]'
        hidden_significance_modal_css = '[data-id=significance_hidden][class*="hidden"]'
        hidden_type_means_modal_css = '[data-id=type_means_hidden][class*="hidden"]'
        hidden_frequency_modal_css = '[data-id=frequency_hidden][class*="hidden"]'
        hidden_assertion_modal_css = '[data-id=assertions_hidden][class*="hidden"]'      
        hidden_categories_modal_css = '[data-id=categories_hidden][class*="hidden"]'
        hidden_principal_assessor_modal_css = '[data-id=principal_assessor_hidden][class*="hidden"]'
        hidden_secondary_assessor_modal_css = '[data-id=secondary_assessor_hidden][class*="hidden"]'       
        hidden_company_modal_css = '[data-id=company_hidden][class*="hidden"]'
        hidden_enabled_user_modal_css = '[data-id=enabled_user_hidden][class*="hidden"]'
        hidden_status_modal_css = '[data-id=status_hidden][class*="hidden"]'
        hidden_auto_generate_modal = '//input[@data-id="auto_generate_chkbx"]/../../../div[contains(@class,"hidden")]'
        hidden_planned_start_date_modal_css = '[data-id=planned_start_date_hidden][class*="hidden"]'
        hidden_planned_end_date_modal_css = '[data-id=planned_end_date_hidden][class*="hidden"]'
        hidden_planned_report_period_from_modal_css = '[data-id=planned_report_period_from_hidden][class*="hidden"]'
        hidden_auditors_modal_css = '[data-id=auditors_hidden][class*="hidden"]'
        hidden_audit_firm_modal_css = '[data-id=audit_firm_hidden][class*="hidden"]'
        hidden_email_preferences_modal_css = '[data-id=email_preferences_hidden][class*="hidden"]'
        hidden_first_task_groups_title_modal_css = '[data-id=first_task_group_title_hidden][class*="hidden"]'
        hidden_custom_email_message_modal_css = '[data-id=custom_start_workflow_email_message_hidden][class*="hidden"]'   
        hidden_auditor_add_css = '[data-id=auditors_hidden][class*="hidden"]'

        hide_kind_nature_modal_css = '[data-id=hide_kind_nature_lk]'
        hide_fraud_related_modal_css = '[data-id=hide_fraud_related_lk]'
        hide_significance_modal_css = '[data-id=hide_significance_lk]'
        hide_type_means_modal_css = '[data-id=hide_type_means_lk]'
        hide_frequency_modal_css = '[data-id=hide_frequency_hidden_lk]'
        hide_frequency_dd_modal_css = '[data-id=hide_frequency_lk]'
        hide_assertion_modal_css = '[data-id=hide_assertions_lk]'        
        hide_categories_modal_css = '[data-id=hide_categories_lk]'
        hide_principal_assessor_modal_css = '[data-id=hide_principal_assessor_lk]'
        hide_secondary_assessor_modal_css = '[data-id=hide_secondary_assessor_lk]'        
        hide_company_modal_css = '[data-id=hide_company_lk]'
        hide_enabled_user_modal_css = '[data-id=hide_enabled_user_lk]'
        hide_status_modal_css = '[data-id=hide_status_lk]'
        hide_auto_generate_modal = '//input[@data-id="auto_generate_chkbx"]/../a'
        hide_planned_start_date_modal_css = '[data-id=hide_planned_start_date_lk]'
        hide_planned_end_date_modal_css = '[data-id=hide_planned_end_date_lk]'
        hide_planned_report_period_from_modal_css = '[data-id=hide_planned_report_period_from_lk]'
        hide_planned_report_period_to_modal_css = '[data-id=hide_planned_report_period_to_lk]'
        hide_auditors_modal_link = '//a[@data-id="add_auditor"]/../..//label/a'
        hide_audit_firm_modal_css = '[data-id=hide_audit_firm_lk]'
        hide_email_preferences_modal_css = '[data-id=hide_email_preferences_lk]'
        hide_first_task_groups_title_modal_css = '[data-id=hide_first_task_group_title_lk]'
        hide_custom_email_message_modal_css = '[data-id=hide_custom_start_workflow_email_message_lk]'       
        # hide links on modal
        hide_owner_modal = '//a[@data-id="hide_owner_lk"]'
        hide_contact_modal = '//a[@data-id="hide_contact_lk"]'
        hide_url_modal = '//a[@data-id="hide_url_lk"]'
        hide_reference_url_modal = '//a[@data-id="hide_reference_url_lk"]'  
        hide_program_reference_url_modal = 'reference_url' #original id    
        hide_code_modal = '//a[@data-id="hide_code_lk"]'
        hide_effective_date_modal = '//a[@data-id="hide_effective_date_lk"]' 
        hide_stop_date_modal = '//a[@data-id="hide_stop_date_lk"]'
        hide_state_modal = '//a[@data-id="hide_state_lk"]'
        hide_description_modal = '//a[@data-id="hide_description_lk"]'
        hide_text_of_section_modal = '//a[@data-id="hide_text_of_section_lk"]'
        hide_note_modal = '//a[@data-id="hide_note_lk"]'
        hide_kind_type_modal = '//a[@data-id="hide_kind_type_lk"]'
        hide_network_zone_modal = '//a[@data-id="hide_network_zone_lk"]'
        hide_private_program_modal = '//a[@data-id="hide_privacy_lk"]'
        help = '//a[@id="page-help" and @data-toggle="modal-ajax-helpform"]'
        help_icon_css = '[class="grcicon-help-black"]'
        edit_help_css = 'a[title="Edit Help"]'
        edit_help_xpath = '//a[@title="Edit Help"]'
        help_done = '//a[@data-dismiss="modal" and @href="javascript://"]'
        save_help_css = '[value=Save]'
        grc_help_title_text_css = 'div[class="modal-header"] span'
        grc_help_content_text_css = '[class="help-content rtf"]'
        help_title_id = 'help_title'
        help_title = '//input[@id="help_title"]'
        help_content = '//textarea[contains(@id,"help_content")]/parent::div/iframe'
        my_tasks_icon = '[class="grcicon-task-black"]'
        #my_tasks_icon = 'a[href="/dashboard#task_widget"]'
        #second_widget = 'ul.nav.internav.cms_controllers_inner_nav li:nth-child(2)'
        #my_tasks_icon = '.header.main ul li'
        start_new_program ='.quick-list a[data-object-plural="programs"]'
        second_widget = '//button[contains(@class, "lhn-trigger pull-left")]'
        filterText = '#program_widget .filter-title > h6'
        
        # CSS and xpaths for new UI
        program_accordion_css = '[data-model-name="Program"]'
        workflow_accordion_css = '[data-model-name="Workflow"]'
        audit_accordion_css = '[data-model-name="Audit"]'
        people_accordion_css = '[class=top-level] > [class="entities accordion-group"]'
        business_accordion_css = '[class=top-level] > [class="business accordion-group"]'
        governance_accordion_css = '[class=top-level] > [class="governance accordion-group"] > a'
        
        #LHN
        obj_regulation_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Regulation] > a[class ='governance list-toggle oneline']"
        obj_regulation_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Regulation] > .content ul li']"
        obj_policy_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Policy] > a[class ='governance list-toggle oneline']"
        obj_policy_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Policy] > .content ul li']"
        obj_standard_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Standard] > a[class ='governance list-toggle oneline']"
        obj_standard_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Standard] > .content ul li']"
        obj_contract_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Contract] > a[class ='governance list-toggle oneline']"
        obj_contract_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Contract] > .content ul li']"
        obj_clause_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Clause] > a[class ='governance list-toggle oneline']"
        obj_clause_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Clause] > .content ul li']"
        obj_section_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Section] > a[class ='governance list-toggle oneline']"
        obj_section_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Section] > .content ul li']"


        obj_control_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Control] > a[class ='controls list-toggle oneline']"
        obj_control_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Control] > .content ul li']"
        obj_objective_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Objective] > a[class ='objectives list-toggle oneline']"
        obj_objective_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Objective] > .objectives ul li']"


        obj_people_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Person] > a[class ='entities list-toggle oneline']"
        obj_people_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Person] > .content ul li']"
        obj_orggroup_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = OrgGroup] > a[class ='entities list-toggle oneline']"
        obj_orggroup_grp_expanded_css = "ul.mid-level.in > li[data-model-name = OrgGroup] > .content ul li']"
        obj_vendor_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Vendor] > a[class ='entities list-toggle oneline']"
        obj_vendor_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Vendor] > .content ul li']"


        obj_system_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = System] > a[class ='business list-toggle oneline']"
        obj_system_grp_expanded_css = "ul.mid-level.in > li[data-model-name = System] > .content ul li']"
        obj_process_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Process] > a[class ='business list-toggle oneline']"
        obj_process_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Process] > .content ul li']"
        obj_dataasset_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = DataAsset] > a[class ='business list-toggle oneline']"
        obj_dataasset_grp_expanded_css = "ul.mid-level.in > li[data-model-name = DataAsset] > .content ul li']"
        obj_product_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Product] > a[class ='business list-toggle oneline']"
        obj_product_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Product] > .content ul li']"
        obj_project_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Project] > a[class ='business list-toggle oneline']"
        obj_project_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Project] > .content ul li']"
        obj_facility_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Facility] > a[class ='business list-toggle oneline']"
        obj_facility_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Facility] > .content ul li']"
        obj_market_grp_collapsed_css = "ul.mid-level.in > li[data-model-name = Market] > a[class ='business list-toggle oneline']"
        obj_market_grp_expanded_css = "ul.mid-level.in > li[data-model-name = Market] > .content ul li']"


        obj_program_grp_expanded_css = '[class="programs list-toggle active"][data-object-singular="Program"]'
        obj_program_grp_collapsed_css = '[class="programs list-toggle oneline"][data-object-singular="Program"]'
        obj_workflow_grp_expanded_css = '[class="programs list-toggle active"][data-object-singular="Workflow"]'
        obj_workflow_grp_collapsed_css = '[class="programs list-toggle oneline"][data-object-singular="Workflow"]'
        obj_audit_grp_expanded_css = '[class="programs list-toggle active"][data-object-singular="Audit"]'
        obj_audit_grp_collapsed_css = '[class="programs list-toggle oneline"][data-object-singular="Audit"]'
        obj_controlassessment_grp_expanded_css = '[class="programs list-toggle active"][data-object-singular="ControlAssessment"]'
        obj_controlassessment_grp_collapsed_css = '[class="programs list-toggle oneline"][data-object-singular="ControlAssessment"]'
        obj_issue_grp_expanded_css = '[class="programs list-toggle active"][data-object-singular="Issue"]'
        obj_issue_grp_collapsed_css = '[class="programs list-toggle oneline"][data-object-singular="Issue"]'


        '''

        obj_ctrl_objectives_grp_collapsed_css = 'li:nth-child(2)  [class="governance list-toggle top"]'
        obj_ctrl_objectives_grp_expanded_css = 'li:nth-child(2)  [class="governance list-toggle top active"]'        
        obj_people_grp_collapsed_css = '[class="entities list-toggle top"]'
        obj_people_grp_expanded_css = '[class="entities list-toggle top active"]'        
        obj_asset_business_grp_collapsed_css = '[class="business list-toggle top"]'                  
        obj_asset_business_grp_expanded_css = '[class="business list-toggle top active"]'
        obj_workflow_grp_expanded_css = '[class="workflow oneline list-toggle active"]'
        obj_workflow_grp_collapsed_css = '[class="workflow oneline list-toggle"]'
        obj_program_grp_expanded_css = '[class="programs list-toggle active"][data-object-singular="Program"]'
        obj_program_grp_collapsed_css = '[class="programs list-toggle oneline"][data-object-singular="Program"]'
        obj_audit_grp_expanded_css = '[class="programs list-toggle oneline active"][data-object-singular="Audit"]'
        obj_audit_grp_collapsed_css = '[class="programs list-toggle"][data-object-singular="Audit"]'

        '''

        page_edit_gear_icon_css =  '[class=details-wrap] [data-toggle=dropdown]' #'[class=grcicon-setup-color]'
        page_edit_link_css = '[class=dropdown-menu] [data-modal-reset=reset]'
        edit_authorization_link_in_DB_css = '[class=dropdown-menu] [data-modal-selector-options=user_roles]'
        edit_person_link_in_DB_css = '[class=dropdown-menu] [data-object-singular=Person]'
        page_edit_gear_icon_wf_css =  '[class="pin-content cms_controllers_info_pin"] [class=details-wrap] [data-toggle=dropdown]'
        edit_task_group_wf_lk_css = '[class=dropdown-menu] [data-modal-reset=reset][data-object-singular=TaskGroup]'
        submit_for_review_css = '[class=non-transparent]'
        add_owner_css = '[data-id=owner_hidden] [class="btn btn-small btn-draft"]'
        owner_textbox_css = '[data-id=owner_txtbx]'
        owner_delete_1st_icon_css = '[class=grcicon-deleted]'
        widget_edit_gear = '//a[@data-toggle="unmap"]/../../../a'
        unmap_lk = '//a[@data-toggle="unmap"]'        
        workflow_draft_link_css = '[data-value=Draft]'
        workflow_active_link_css = '[data-value=Active]'
        workflow_inactive_link_css = '[data-value=Inactive]'
        audit_program_dropdown_css = '[data-id=program_dd]' # on audit modal
        add_person_plus_sign_DB = '//a[(@data-original-title="Add Person")]'

        #LHN
        show = 'button.lhn-trigger.active'
        no_show = 'button.lhn-trigger'

        lhn_directive_active='ul.top-level > li.governance.accordion-group > a.governance.list-toggle.top.active'
        lhn_directive_inactive='ul.top-level > li.governance.accordion-group > a.governance.list-toggle.top'

        lhn_control_active='ul.top-level > li.governance.accordion-group:nth-child(2) > a.governance.list-toggle.top.active'
        lhn_control_inactive='ul.top-level > li.governance.accordion-group:nth-child(2) > a.governance.list-toggle.top'

        lhn_people_active='ul.top-level > li.entities.accordion-group > a.entities.list-toggle.top.active'
        lhn_people_inactive='ul.top-level > li.entities.accordion-group > a.entities.list-toggle.top'

        lhn_asset_active='ul.top-level > li.business.accordion-group > a.business.list-toggle.top.active'
        lhn_asset_inactive='ul.top-level > li.business.accordion-group > a.business.list-toggle.top'

        #Object Form
        #object_title = "input[data-id=title_txtbx][name=title]"
        object_title = '//input[@name="title"]'
        
        
        