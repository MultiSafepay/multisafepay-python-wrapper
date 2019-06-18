class Gateways:
    def __init__(self, client):
        self.endpoint = 'gateways'
        self.msp_client = client
        self.method = 'GET'

    def gateway(self, gatewayid):
        endpoint = '{0}/{1}'.format(self.endpoint,gatewayid)
        return self.msp_client.execute_http_call(self.method, endpoint)

    def allgateways(self, *args):
        if not args:
            endpoint = self.endpoint
        else:
            endpoint = '{0}{1}'.format(self.endpoint, *args)
        return self.msp_client.execute_http_call(self.method, endpoint)
