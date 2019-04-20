import twitter
import json

with open('src/secrets.json', encoding='utf-8') as secret_file:
    secrets = json.loads(secret_file.read())


CONSUMER_KEY = secrets['CONSUMER_KEY']
CONSUMER_SECRET = secrets['CONSUMER_SECRET']
ACCESS_TOKEN = secrets['ACCESS_TOKEN']
ACCESS_SECRET = secrets['ACCESS_SECRET']


def respond_to_direct_message(eventBody):
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET)

    dm = twitter.DirectMessage.NewFromJsonDict(eventBody)

    sent_from = eventBody['direct_message_events'][0]['message_create']['sender_id']
    screen_name = eventBody['users'][sent_from]['screen_name']
    text = 'roger roger {}'.format(screen_name)
    sentDm = api.PostDirectMessage(user_id=sent_from,text=text, return_json=True)
    print("this was sent_ ", sentDm)
    return dm

        
