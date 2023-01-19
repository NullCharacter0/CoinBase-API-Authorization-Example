

class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(int(time()))
        message = timestamp + request.method + request.path_url.split('?')[0] + str(request.body or '')
        signature = hmac.new(self.secret_key.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

        request.headers.update({
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
        })
        return request

auth = CoinbaseWalletAuth(api, secretkey)

now = time()
end = str(int(now))
start =  str(int(now)-90000)
base_url = "https://api.coinbase.com/api/v3/brokerage/products/"

get(f"{base_url}{self.currency}/candles?start={start}&end={end}&granularity=FIVE_MINUTE",auth=auth).json()

