import json
import os
import requests


class Client(object):
    client = None
    client_id = ''
    client_secret = ''
    extra_option = None
    REALTOR_IDENTITY_URL = os.environ.get("REALTOR_IDENTITY_URL", "https://identity.crea.ca/connect/token")

    def __init__(self, client_id, client_secret, extra_option=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.extra_option = extra_option

        if self.REALTOR_IDENTITY_URL is None:
            raise ValueError
        pass

    def get_token(self, grant_type='client_credentials', scope='DDFApi_Read'):
        payload = {'grant_type': grant_type, 'scope': scope, 'client_id': self.client_id,
                   'client_secret': self.client_secret}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(self.REALTOR_IDENTITY_URL, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()
