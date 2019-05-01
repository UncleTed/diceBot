class DirectMessageHandler:
    def __init__(self, twitterApi):
        self.api = twitterApi

    def respond_to_direct_message(self, jsonDirectMessage):
        sent_from = jsonDirectMessage['direct_message_events'][0]['message_create']['sender_id']
        screen_name = jsonDirectMessage['users'][sent_from]['screen_name']
        text = 'roger roger {}'.format(screen_name)
        sentDm = self.api.PostDirectMessage(user_id=sent_from, text=text, return_json=False)
