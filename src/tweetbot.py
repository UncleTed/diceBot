from twython import Twython


with open('src/secrets.json', encoding='utf-8') as secret_file:
    secrets = json.loads(secret_file.read())


CONSUMER_KEY = secrets['CONSUMER_KEY']
CONSUMER_SECRET = secrets['CONSUMER_SECRET']
ACCESS_TOKEN = secrets['ACCESS_TOKEN']
ACCESS_SECRET = secrets['ACCESS_SECRET']

twitter_client = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
twitter_client.update_status(status='I saw a man that wasn\'t there')
