import requests
import json

class CoinInfoLoader:
    _END_POINT  = 'https://api.coin.z.com/public'
    _RATE_PATH  = '/v1/ticker?symbol=BTC_JPY'
    _TRACE_PATH = '/v1/trades?symbol=BTC_JPY&page={page}&count={count}'
    
    @classmethod
    def tarde(self, page = 1, count = 100):
        path = self._TRACE_PATH.format(page = 1, count = count)

        response = requests.get(self._END_POINT + path)
        return response.json()
    
    @classmethod
    def rate(self):
        response = requests.get(self._END_POINT + self._RATE_PATH)
        return response.json()
