import json

from src.rollDice import roll_dice
from src.rollDice import ascii_histogram
from src.challenge_response_check import perform_challenge_response_check
from src.direct_message import respond_to_direct_message


def rollTheBones(event, context):

    method = None
    if event['httpMethod'] == 'GET':
        method = 'its a GET'
    else:
        method = 'wat'

    body = {
        "you rolled a ":  roll_dice(),
        "event": event,
        "method": method
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
    }
    return response


def showHistogram(event, context):
    histogram = ascii_histogram()
    response = {
        "statusCode": 200,
        "body": histogram
    }
    return response


def webhook(event, context):
    print(event)
    return perform_challenge_response_check(event)


def directMessage(event, context):
    response = {
        'statusCode': 200,
        'body': json.dumps(event)
    }

    if 'direct_message_indicate_typing_events' in event['body']:
        print('direct_message_indicate_typing_events')
    elif 'direct_message_events' in event['body']:
        theBody = json.loads(event['body'])
        if theBody['direct_message_events'][0]['message_create']['target']['recipient_id'] == '1111446422707204096':
            respond_to_direct_message(theBody)
        else:
            print('from myself')

    else:
        print(event['body'])

    return response


if __name__ == "__main__":
    print(rollTheBones(None, None))
