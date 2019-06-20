class Issuers:
    def __init__(self, client):
        self.endpoint = 'issuers/ideal'
        self.msp_client = client
        self.method = 'GET'

    def get(self):
        endpoint = '{0}'.format(self.endpoint)
        return self.msp_client.execute_http_call(self.method, endpoint)

