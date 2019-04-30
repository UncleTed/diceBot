import unittest
import json
import twitter
import ast
from unittest.mock import patch
from unittest.mock import Mock
from src.direct_message import respond_to_direct_message


class direct_message_test(unittest.TestCase):

    def test_respond_to_directMessage(self):
        with open('test_data/direct_messages/direct_message.txt', encoding='utf-8') as direct_message_file:
            direct_message_as_string = direct_message_file.read()
        event = ast.literal_eval(direct_message_as_string)
        mock_post = Mock()
        with patch('twitter.Api.PostDirectMessage') as mock_post:
            respond_to_direct_message(json.loads(event['body']))
            mock_post.assert_called_with(user_id='125505243', text='roger roger UncleTedly', return_json=False)

        dm = respond_to_direct_message(event['body'])
        self.assertIsInstance(dm, twitter.models.DirectMessage, msg='Instead it was a {}'.format(type(dm)))
        # self.assertEqual('roger roger UncleTedly',dm.text)
        # self.assertEqual('1111446422707204096', dm.sender_id)

    
