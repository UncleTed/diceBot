import base64
import hmac
import hashlib
import json


def perform_challenge_response_check(event):
    with open('src/secrets.json', encoding='utf-8') as secret_file:
        secrets = json.loads(secret_file.read())

    if event['httpMethod'] == 'GET':
        if 'queryStringParameters' in event:
            crc = event['queryStringParameters']['crc_token']
            secret = secrets['CRC_SECRET']
            sha256_hash_digest = hmac.new(
                secret.encode('utf-8'), msg=crc.encode('utf-8'),
                digestmod=hashlib.sha256).digest()

            body = json.dumps({
                'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest).decode('utf-8')
            })
            
            response = {
                'statusCode': 200,
                'body': body
            }

    
            return response
        else:
            return None
    else:
        return None
