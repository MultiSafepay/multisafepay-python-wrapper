from multisafepay.client import Client

msp_client = Client()
# Here you can set the mode to TEST or LIVE based on the API you want to use
msp_client.set_modus('TEST')
msp_client.set_api_key('REPLACE WITH API KEY')

# to update a existing order use the following example
print(msp_client.order.update(49, {
    "status":"shipped",
    "tracktrace_code":"3SMSP0123456789",
    "carrier":"MSP Logistics",
    "ship_date":"01-01-1911",
    "reason":"Fulfilled by warehouse",
    "invoice_id":"AB12345"
}))
