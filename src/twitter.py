from requests_oauthlib import OAuth1Session
import urllib
import json

with open('src/secrets.json', encoding='utf-8') as secret_file:
    secrets = json.loads(secret_file.read())

CONSUMER_KEY = secrets['CONSUMER_KEY']
CONSUMER_SECRET = secrets['CONSUMER_SECRET']
ACCESS_TOKEN = secrets['ACCESS_TOKEN']
ACCESS_SECRET = secrets['ACCESS_SECRET']

twitter = OAuth1Session(CONSUMER_KEY,
                        client_secret=CONSUMER_SECRET,
                        resource_owner_key=ACCESS_TOKEN,
                        resource_owner_secret=ACCESS_SECRET)
#webhook_endpoint = urllib.parse.quote_plus('https://fm0fxa866m.execute-api.us-west-2.amazonaws.com/dev/webhook')
# url = 'https://api.twitter.com/1.1/account_activity/all/dev/webhooks.json?url={}'.format(webhook_endpoint)
# url = 'https://api.twitter.com/1.1/account_activity/all/dev/subscriptions.json'
url = 'https://api.twitter.com/1.1/account_activity/all/dev/webhooks/1114560333870399488.json'
#response = twitter.post(url)

response = twitter.put(url)
print(response.status_code," ", response.reason, " ", response.text)
print(response.request.headers)
print(response.request.url)
print("request body ", response.request.body)
