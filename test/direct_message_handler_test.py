import unittest
import json
import twitter
import ast
from unittest.mock import patch
from unittest.mock import Mock
from src.direct_message_handler import DirectMessageHandler


class direct_message_handler_test(unittest.TestCase):

    def test_respond_to_directMessage(self):
        mock_api = Mock()
        
        directMessageHandler = DirectMessageHandler(mock_api)
        with open('test_data/direct_messages/direct_message.txt', encoding='utf-8') as direct_message_file:
            direct_message_as_string = direct_message_file.read()
        event = ast.literal_eval(direct_message_as_string)
        directMessageHandler.respond_to_direct_message(json.loads(event['body']))
        mock_api.PostDirectMessage.assert_called_with(user_id='125505243', text='roger roger UncleTedly', return_json=False)