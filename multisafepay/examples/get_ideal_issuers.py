from multisafepay.client import Client

msp_client = Client()
# Here you can set the mode to TEST or LIVE based on the API you want to use
msp_client.set_modus('TEST')
msp_client.set_api_key('REPLACE WITH API KEY')
# To retrieve a list of all the iDEAL issuers you can use the following example
print(msp_client.ideal_issuers.get())