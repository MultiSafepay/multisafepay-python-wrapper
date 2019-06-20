from multisafepay.client import Client

msp_client = Client()
# Here you can set the mode to TEST or LIVE based on the API you want to use
msp_client.set_modus('TEST')
msp_client.set_api_key('REPLACE WITH API KEY')

# The following code will create a iDEAL order
print(msp_client.order.create({
    "type": msp_client.ordertype.REDIRECT,
    "order_id": "my-order-id-1",
    "gateway": msp_client.paymentmethod.IDEAL,
    "currency": "EUR",
    "amount": "1000",
    "description": "Test Order Description",
    "payment_options": {
        "notification_url": "https://www.example.com/client/notification?type=notification",
        "redirect_url": "https://www.example.com/client/notification?type=redirect",
        "cancel_url": "https://www.example.com/client/notification?type=cancel"
    },
    "customer": {
        "locale": "en_US"
    }
}))

