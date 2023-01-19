from hmac import new
from hashlib import sha256
from time import time
from requests import get
from requests.auth import AuthBase 



# https://docs.cloud.coinbase.com/sign-in-with-coinbase/docs/api-key-authentication


# GET https://api.coinbase.com/v2/accounts

api_url = "https://api.coinbase.com/v2/accounts"
api = 'API_KEY' # !!!!!!!
secretkey = 'SECRET_KEY' # !!!!!!!
# Create custom authentication for Coinbase API


class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(int(time()))
        message = timestamp + request.method + request.path_url + (request.body or '')
        signature = new(self.secret_key.encode('utf-8'), message.encode('utf-8'), sha256).hexdigest()

        request.headers.update({
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
        })
        return request

auth = CoinbaseWalletAuth(api, secretkey)



# Get current user
r = get(api_url,auth=auth)

print(r.json() if r.status_code ==200 else (r.status_code, r.text) )
