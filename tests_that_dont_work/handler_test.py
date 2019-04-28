import unittest
import json
import sys
import os

from handler import directMessage

class handler_test(unittest.TestCase):
    def test_respond_to_directMessage(self):
        jsonFile = './test_data/direct_messages/direct_message.json'
        with open(jsonFile) as f:
            resp_data = f.read()
        someJson = json.loads(resp_data)
        print ('type of someJson is ', type(someJson))
        self.assertIsInstance(someJson, dict, msg='Instead it was a {}'.format(type(someJson)))
        message = directMessage(someJson, {})
        # # print(message)
        # self.assertEquals(200, message['status_code'])



        
