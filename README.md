<p align="center">
  <img src="https://www.multisafepay.com/img/multisafepaylogo.svg" width="400px" position="center">
</p>

# Python wrapper for the MultiSafepay API
This wrapper simplifies working with the MultiSafepay API and allows you to integrate MultiSafepay within your Python application.
## About MultiSafepay ##
MultiSafepay is a collecting payment service provider which means we take care of the agreements, technical details and payment collection required for each payment method. You can start selling online today and manage all your transactions from one place.
## Requirements
- To use the wrapper you need a MultiSafepay account. You can create a test account on https://testmerchant.multisafepay.com/signup.
- Python 3.6 or higher
- Packages: requests
## Installation
Clone this git repository and make sure you meet the requirements, viinstallation through pip will be added in a future release. 
## Usage
Setup the client for testing
```python
from multisafepay.client import Client
msp_client = Client()
msp_client.set_modus('TEST')
msp_client.set_api_key('REPLACE WITH API KEY')
```
Creating a test order 
```
# The following code will create a iDEAL order
print(msp_client.order.create({
    "type": msp_client.ordertype.DIRECT,
    "order_id": "my-order-id-1",
    "gateway": msp_client.paymentmethod.KLARNA,
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
```
Click [here](https://github.com/MultiSafepay/multisafepay-python-wrapper/tree/master/multisafepay/examples) for more examples.
## Support
If you have any issues, problems or questions you can create an issue on this repository or contact us at <a href="mailto:techsupport@multisafepay.com">techsupport@multisafepay.com</a>.

## Mistakes and improvements 
If you spot mistakes or want to contribute in improving this wrapper, feel free to [create pull requests](https://github.com/MultiSafepay/multisafepay-python-wrapper/pulls)!

## API Documentation
[Click here](https://docs.multisafepay.com/api/) for the MultiSafepay API documentation.
## License
[MIT License](https://github.com/MultiSafepay/multisafepay-python-wrapper/blob/master/LICENSE)
