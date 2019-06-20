from multisafepay.client import Client

msp_client = Client()
# Here you can set the mode to TEST or LIVE based on the API you want to use
msp_client.set_modus('TEST')
msp_client.set_api_key('REPLACE WITH API KEY')

# The following code will create a iDEAL order with ING as issuer
# Issuers can only be used with iDEAL
print(msp_client.order.create({
    "type": msp_client.ordertype.REDIRECT,
    "order_id": "My-order-id-5",
    "currency": "EUR",
    "amount": 1000,
    "gateway": msp_client.paymentmethod.IDEAL,
    "description": "product description",
    "gateway_info": {
        "issuer_id": msp_client.issuer.ING
    },
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": False
    }
}))

