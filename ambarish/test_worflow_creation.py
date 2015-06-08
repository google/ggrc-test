__author__ = 'asakhare'
import unittest
import requests
import json
from nose.plugins.skip import SkipTest
#from ggrc_workflows.models import *


class TestWorkflowCreation(unittest.TestCase):
    def setUp(self):
        self.api = Api()
        person = {'name': 'xyz', 'email':'xyz'}
        self.api.set_user(self, person=person)
        self.create_app()
    def tearDown(self):
        pass
    '''
    def _workflow_factory(self):
        workflow = Workflow()
        workflow.id = 1
        workflow.frequency = "one_time"
        workflow.title = "One Time Workflow"
        return workflow
    '''
    @SkipTest
    def testWithSysWideReaderRole(self):
        #api_response= self._workflow_factory()
        request_url= "http://localhost:8080/api/workflows"
        payload= {"workflow":{"custom_attribute_definitions":[],"custom_attributes":{},"_transient":{},"title":"hhhhhhhhh","description":"","frequency":"one_time","notify_on_change":False,"task_group_title":"Task Group 1","notify_custom_message":"","owners":None,"context":None,"provisional_id":"provisional_9950553"}}
        headers={'Accept':'application/json'}
        response = requests.post(request_url, data=json.dumps(payload),headers=headers)
        self.assertEqual(response.status_code, 200, 'http request is unsuccessful, the response status code is ' +str(response.status_code))
        print response.status_code

    def testMapping(self):
        #api_response= self._workflow_factory()
        request_url= "http://grc-test.appspot.com/api/program_directives"
        payload= {"program_directive":{"directive":{"id":8763,"href":"/api/policies/8763","type":"Policy"},"program":{"id":3853,"href":"/api/programs/3853","type":"Program"},"context":{"id":9419,"href":"/api/contexts/9419","type":"Context"},"provisional_id":"provisional_8890298"}}
        headers={'Accept':'application/json', "X-Requested-By": "gGRC", 'Content-type': 'application/json'}
        response = requests.post(request_url, data=json.dumps(payload),headers=headers)
        self.assertEqual(response.status_code, 200, 'http request is unsuccessful, the response status code is ' +str(response.status_code))
        print response.status_code
        print response._content
