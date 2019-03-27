import json
from src.rollDice import roll_d20


def rollTheBones(event, context):

    body = {
        "you rolled a ":  roll_d20(),
        "event": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
    }
    return response


if __name__ == "__main__":
    print(rollTheBones(None, None))