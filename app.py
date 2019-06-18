from multisafepay.client import Client

msp_client = Client()
#fill in TEST API key here
msp_client.set_api_key('')

print(msp_client.order.create({
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": msp_client.paymentmethod.EPS,
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

print(msp_client.gateways.gateways(country='NL',currency='100'))
