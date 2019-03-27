import json
import rollDice


def rollTheBones(event, context):

    rollDice.roll_d20()
    body = {
        "you rolled a ":  rollDice.roll_d20(),
        "event": event,
        "context": context
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response


if __name__ == "__main__":
    print(rollTheBones(None, None))