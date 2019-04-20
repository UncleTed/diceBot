import unittest
import json
from src.challenge_response_check import perform_challenge_response_check


class challenge_response_check_test(unittest.TestCase):
    def test_response_for_crc_when_get(self):
        body = json.dumps({'response_token': 'sha256=eOhMahT9SIONh0eYAH1XcoZORvpEstfdYU4Z8gGZhOo='})
        expected = {
            "statusCode": 200,
            "body": body,
        }

        event = {
            'httpMethod': 'GET',
            'queryStringParameters': {
                'crc_token': 'blahblah',
                'nonce': 'mcmllvv'
            }
        }
 
        actual = perform_challenge_response_check(event)
        
        self.assertEqual(expected, actual)
    
    def test_response_when_post(self):
        event = {
            'httpMethod': 'POST',
            'queryStringParameters': {
                'crc_token': 'blahblah',
                'nonce': 'mcmllvv'
            }
        }
        actual = perform_challenge_response_check(event)
        self.assertEqual(None, actual)