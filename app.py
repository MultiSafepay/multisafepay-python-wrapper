from multisafepay.client import Client

msp_client = Client()
msp_client.set_api_key('')

data = {}
print(msp_client.order.create(data))

