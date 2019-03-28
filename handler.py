import json
from src.rollDice import roll_dice
from src.rollDice import ascii_histogram


def rollTheBones(event, context):

    body = {
        "you rolled a ":  roll_dice(),
        "event": event
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

if __name__ == "__main__":
    print(rollTheBones(None, None))