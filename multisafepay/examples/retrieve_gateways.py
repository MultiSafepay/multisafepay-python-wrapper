from multisafepay.client import Client

msp_client = Client()
# Here you can set the mode to TEST or LIVE based on the API you want to use
msp_client.set_modus('TEST')
msp_client.set_api_key('REPLACE WITH API KEY')

# To retrieve all the gateways you can use the following
print(msp_client.gateways.allgateways())
# To use filters use the following code
print(msp_client.gateways.allgateways('?country=BE&currency=EUR&amount=10000'))
# To retrieve information about one gateway use the following
print(msp_client.gateways.gateway('IDEAL'))
