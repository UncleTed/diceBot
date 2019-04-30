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
        
        message = directMessage(resp_data, {})
        # print(message)

    def test_current_working_directory(self):
        print(sys.path)


        
