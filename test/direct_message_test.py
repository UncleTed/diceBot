import unittest
import json
import twitter
from src.direct_message import respond_to_direct_message

class direct_message_test(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(1,1)
    def test_respond(self):
        self.assertEqual(1,1)
        json_from_twitter = {
            "for_user_id": "1111446422707204096",
            "direct_message_events": [
                {"type": "message_create",
                 "id": "1116180319856623620",
                 "created_timestamp": "1554953100538",
                 "message_create": {
                     "target": {
                         "recipient_id": "1111446422707204096"
                     },
                     "sender_id": "125505243",
                     "message_data": {
                         "text": "Woot",
                         "entities": {
                             "hashtags": [],
                             "symbols":[],
                             "user_mentions":[],
                             "urls":[]
                         }
                     }
                 }
                 }
            ],
            "users": {
                "125505243": {
                    "id": "125505243",
                    "created_timestamp": "1269306135000",
                    "name": "Ted Layher",
                    "screen_name": "UncleTedly",
                    "location": "Sunny Ypsilanti",
                    "protected": 'false',
                    "verified": 'false',
                    "followers_count": 36,
                    "friends_count": 73,
                    "statuses_count": 121,
                    "profile_image_url": "http:\\/\\/pbs.twimg.com\\/profile_images\\/1229180948\\/IMG_0354_normal.JPG",
                    "profile_image_url_https": "https:\\/\\/pbs.twimg.com\\/profile_images\\/1229180948\\/IMG_0354_normal.JPG"
                },
                "1111446422707204096": {
                    "id": "1111446422707204096",
                    "created_timestamp": "1553824451628",
                    "name": "UncleTedBot",
                    "screen_name": "UncleTedBot1",
                    "description": "I\'m just a bot",
                    "protected": 'false',
                    "verified": 'false',
                    "followers_count": 0,
                    "friends_count": 1,
                    "statuses_count": 1,
                    "profile_image_url": "http:\\/\\/pbs.twimg.com\\/profile_images\\/1111461956479799296\\/QVu5Houu_normal.png",
                    "profile_image_url_https": "https:\\/\\/pbs.twimg.com\\/profile_images\\/1111461956479799296\\/QVu5Houu_normal.png"
                }
            }
        }
        dm = respond_to_direct_message(json_from_twitter)
    #     # print(dm)
        self.assertEqual(1,1)
    
