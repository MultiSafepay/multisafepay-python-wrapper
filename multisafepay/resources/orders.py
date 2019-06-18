class Orders:
    def __init__(self, client):
        self.endpoint = 'orders'
        self.msp_client = client

    def create(self, data):
        method = 'POST'
        return self.msp_client.execute_http_call(method, self.endpoint, data)

    def get(self, order_id):
        endpoint = '{0}/{1}'.format(self.endpoint, order_id)
        method = 'GET'
        return self.msp_client.execute_http_call(method, endpoint)

    def update(self, order_id, data):
        endpoint = '{0}/{1}'.format(self.endpoint, order_id)
        method = 'PATCH'
        return self.msp_client.execute_http_call(method, endpoint, data)

    def refund(self, order_id, data):
        endpoint = '{0}/{1}/refunds'.format(self.endpoint, order_id)
        method = 'POST'
        return self.msp_client.execute_http_call(method, endpoint, data)
