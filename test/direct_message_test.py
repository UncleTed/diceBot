import unittest
import json
import twitter
from src.direct_message import respond_to_direct_message

class direct_message_test(unittest.TestCase):

    def test_respond(self):
        with open('test_data/direct_messages/direct_message.json', encoding='utf-8') as direct_message_file:
            payload_from_lambda = direct_message_file.read()
        event = json.loads(payload_from_lambda) 

        dm = respond_to_direct_message(event['body'])
        self.assertIsInstance(dm, twitter.models.DirectMessage, msg='Instead it was a {}'.format(type(dm)))
        # self.assertEqual('roger roger UncleTedly',dm.text)
        # self.assertEqual('1111446422707204096', dm.sender_id)

    
