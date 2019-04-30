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
    #     # print(dm)
        self.assertIsInstance(dm, twitter.DirectMessage)
        # self.assertEqual('foo', dm)
