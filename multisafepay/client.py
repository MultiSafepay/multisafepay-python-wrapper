from multisafepay.resources.orders import Orders
from multisafepay.resources.gateways import Gateways
from multisafepay.resources.ideal_issuers import Issuers
from multisafepay.objects.paymentmethod import PaymentMethod
from multisafepay.objects.issuers import Issuer
from multisafepay.objects.ordertype import OrderType
import requests
import json


class Client:
    def __init__(self, modus=None, api_key=None):
        self.modus = modus
        self.api_url = None
        self.api_key = api_key
        self.paymentmethod = PaymentMethod
        self.issuer = Issuer
        self.ordertype = OrderType
        self.order = Orders(self)
        self.gateways = Gateways(self)
        self.ideal_issuers = Issuers(self)

    def set_api_key(self, api_key):
        self.api_key = self.validate_api_key(api_key)

    def set_modus(self, modus):
        self.modus = modus
        if self.modus is 'TEST':
            self.api_url = 'https://testapi.multisafepay.com/v1/json'
        elif self.modus is 'LIVE':
            self.api_url = 'https://api.multisafepay.com/v1/json'
        else:
            raise ValueError('Invalid API mode, needs to be LIVE or TEST')

    @staticmethod
    def validate_api_key(api_key):
        api_key = api_key.strip()
        if len(api_key) != 40:
            raise ValueError("Invalid API key: '{api_key}'. An API key must be 40 "
                             "characters long".format(api_key=api_key))
        return api_key

    def execute_http_call(self, http_method, endpoint, data=None, **kwargs):
        response = requests.request(http_method,
                                    url='{0}/{1}'.format(self.api_url, endpoint),
                                    headers={'api_key':'{api_key}'.format(
                                        api_key=self.api_key)}, json=data, **kwargs)
        json_data = json.loads(response.text)
        return json_data
