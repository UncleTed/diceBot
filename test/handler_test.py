import unittest
import ast
import handler
from unittest.mock import Mock
from unittest.mock import patch

class handler_test(unittest.TestCase):
    def test_direct_message(self):
        mock_respond = Mock()
        jsonFile = './test_data/direct_messages/direct_message.txt'
        with open(jsonFile) as f:
            resp_data = f.read()
        self.assertEqual(4510, len(resp_data))
        self.assertIsInstance(resp_data, str)

        with patch('src.direct_message.respond_to_direct_message') as mock_respond:
            message = handler.directMessage(ast.literal_eval(resp_data), {})
            mock_respond.assert_called_with('foo')
        # print(message)


        
