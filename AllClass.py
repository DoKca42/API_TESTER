import base64
import json
from datetime import datetime, timedelta

import requests
from amqp import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timezone
import random

BLOCKCHAIN_URL = "http://k1r4p6"
BLOCKCHAIN_HOST = "8020"
ROOMMANAGER_URL = "http://localhost"
ROOMMANAGER_HOST = "8000"
NGN_URL = "http://localhost"
NGN_HOST = "8056"

class Uniqid:

    @staticmethod
    def __getRandom():
        random_number = random.randint(0, 99)
        formatted_number = str(random_number).zfill(2)
        return formatted_number

    @staticmethod
    def getUnixTimeStamp():
        now_utc = datetime.now(timezone.utc)
        unix_timestamp = int(now_utc.timestamp())
        return unix_timestamp

    @staticmethod
    def generate():
        uniqid = Uniqid.__getRandom() + Uniqid.__getRandom()
        uniqid += str(Uniqid.getUnixTimeStamp())
        uniqid += Uniqid.__getRandom() + Uniqid.__getRandom()
        return uniqid


class Signature:
    def __init__(self):
        pass

    @staticmethod
    def getPrivateKey():
        f = open("private_key.pem", "rb")
        load_key = load_pem_private_key(f.read(), None)
        return load_key

    @staticmethod
    def create_signed_token(data, life_span_minutes=5):
        private_key = Signature.getPrivateKey()

        data['transaction_id'] = Uniqid.generate()
        data['expires'] = (datetime.utcnow() + timedelta(minutes=life_span_minutes)).isoformat()
        data_json = json.dumps(data)

        data_bytes = data_json.encode('utf-8')
        signature = private_key.sign(
            data_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        signature_encoded = base64.b64encode(signature).decode('utf-8')
        return data, signature_encoded


def postMatch_ToBC(match):
    print("[INPUT] match ", match)
    try:
        data, signature = Signature.create_signed_token(match)

        headers = {"Authorization": str(signature)}
        host = BLOCKCHAIN_URL + ":" + BLOCKCHAIN_HOST
        url = host + '/match/post/'
        x = requests.post(url, json=data, headers=headers)
        print("[SUCCESS] Post ", x)
    except Exception as e:
        print("[ERROR] Post ", e)


def postMatch_ToRM(match):
    print("[INPUT] match ", match)
    try:
        data, signature = Signature.create_signed_token(match)

        headers = {"Authorization": str(signature)}
        host = ROOMMANAGER_URL + ":" + ROOMMANAGER_HOST
        url = host + '/api/match_result/'
        x = requests.post(url, json=data, headers=headers)
        print("[SUCCESS] Post ", x)
    except Exception as e:
        print("[ERROR] Post ", e)


def postMatch_ToNGN(match):
    print("[INPUT] match ", match)
    try:
        data, signature = Signature.create_signed_token(match)

        headers = {"Authorization": str(signature),
                   "TransactionId": str(Uniqid.generate()),
        host = NGN_URL + ":" + NGN_HOST
        url = host + '/api/create_game/'
        x = requests.post(url, json=data, headers=headers)
        print("[SUCCESS] Post ", x)
    except Exception as e:
        print("[ERROR] Post ", e)
