from multisafepay.resources.orders import Orders
from multisafepay.objects.paymentmethod import PaymentMethod
from multisafepay.resources.gateways import Gateways
import requests
import json


class Client:
    def __init__(self, api_key=None):
        self.api_url = 'https://testapi.multisafepay.com/v1/json'
        self.api_key = api_key
        self.order = Orders(self)
        self.paymentmethod = PaymentMethod
        self.gateways = Gateways(self)

    def set_api_key(self, api_key):
        self.api_key = self.validate_api_key(api_key)

    @staticmethod
    def validate_api_key(api_key):
        api_key = api_key.strip()
        if len(api_key) != 40:
            raise ValueError("Invalid API key: '{api_key}'. An API key must be 40 "
                             "characters long".format(api_key=api_key))
        return api_key

    def execute_http_call(self, http_method, endpoint, data=None,**kwargs):
        response = requests.request(http_method,
                                    url='{0}/{1}'.format(self.api_url, endpoint),
                                    headers={'api_key':'{api_key}'.format(
                                        api_key=self.api_key)}, json=data,**kwargs)
        json_data = json.loads(response.text)
        return json_data
