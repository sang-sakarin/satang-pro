"""
A libraly that provides a python interface to Satang Pro API
"""
from .constants import ENDPOINTS
from .decorators import check_in_kwargs
from .request import basic_request


class SatangPro:
    @check_in_kwargs(["api_key", "secret_key"])
    def __init__(self, api_key='', secret_key=''):
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        self.API_ROOT = ENDPOINTS["API_ROOT"]

    def _get_path(self, path_name, **kwargs):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name].format(**kwargs)

    @check_in_kwargs(["pair"])
    def orders(self, pair=''):
        url = self._get_path("ORDERS_PATH", pair=pair)

        return basic_request('GET', url)

    def orderbook_tickers(self):
        url = self._get_path("ORDERBOOK_TICKERS_PATH")

        return basic_request('GET', url)
