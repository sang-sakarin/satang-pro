"""
A libraly that provides a python interface to Satang Pro API
"""
import hashlib
import hmac

from .constants import ENDPOINTS
from .decorators import check_in_kwargs
from .request import basic_request


class SatangPro:
    @check_in_kwargs(["api_key", "secret_key"])
    def __init__(self, api_key='', secret_key=''):
        self.api_key = api_key
        self.api_secret = secret_key
        self.API_ROOT = ENDPOINTS["API_ROOT"]

    def _get_path(self, path_name, **kwargs):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name].format(**kwargs)

    def _get_api_secret(self):
        return self.api_secret.encode()

    def _get_signature(self, payload):
        signature = hmac.new(self._get_api_secret(), msg=payload.encode(), digestmod=hashlib.sha512).hexdigest()

        return signature

    def _get_headers(self, signature=''):
        headers = {}
        headers["Authorization"] = "TDAX-API {0}".format(self.api_key)
        headers["Signature"] = signature

        return headers

    @check_in_kwargs(["pair"])
    def orders(self, pair=''):
        url = self._get_path("ORDERS_PATH", pair=pair)

        return basic_request('GET', url)

    def orderbook_tickers(self):
        url = self._get_path("ORDERBOOK_TICKERS_PATH")

        return basic_request('GET', url)

    def users(self):
        url = self._get_path("USERS_PATH", id=None)
        signature = self._get_signature('')
        headers = self._get_headers(signature=signature)

        return basic_request('GET', url, headers=headers)
