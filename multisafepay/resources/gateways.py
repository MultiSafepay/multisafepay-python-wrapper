class Gateways:
    def __init__(self, client):
        self.endpoint = 'gateways'
        self.msp_client = client
        self.method = 'GET'

    def gateway(self, gatewayid):
        self.endpoint = '{0}/{1}'.format(self.endpoint,gatewayid)
        return self.msp_client.execute_http_call(self.method, self.endpoint)

    def gateways(self, country=None, currency=None, amount=None, include=None):
        if country or currency or amount or include:
            self.endpoint = '{0}?'.format(self.endpoint)
        if country:
            self.endpoint = '{0}country={1}'.format(self.endpoint, country)
        if currency:
            self.endpoint = '{0}&currency={1}'.format(self.endpoint, currency)
        if amount:
            self.endpoint = '{0}&amount={1}'.format(self.endpoint, amount)
        if include:
            self.endpoint = '{0}&include={1}'.format(self.endpoint, include)
        return self.msp_client.execute_http_call(self.method, self.endpoint)
