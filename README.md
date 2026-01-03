# This project has been archived.
# The maintainers of this project have marked this project as archived. No new releases are expected.

---
# SendCloud
![Python package](https://github.com/stasfilin/sendcloud/workflows/Python%20package/badge.svg?branch=master)
[![Downloads](https://pepy.tech/badge/sendcloud-python)](https://pepy.tech/project/sendcloud-python)
[![Downloads](https://pepy.tech/badge/sendcloud-python/month)](https://pepy.tech/project/sendcloud-python)
[![Downloads](https://pepy.tech/badge/sendcloud-python/week)](https://pepy.tech/project/sendcloud-python)

[![sendcloud-python](https://snyk.io/advisor/python/sendcloud-python/badge.svg)](https://snyk.io/advisor/python/sendcloud-python)


Unofficial Python Library

This is a Python library that provides a simple way to communicate with the Sendcloud API. 

## Installation 
```sh
pip install sendcloud-python
```

## Example

```python
import sendcloud
from sendcloud.classes import Parcels

sendcloud.API_KEY = "TEST_KEY"
sendcloud.API_SECRET = "TEST_SECRET"

parcels = Parcels().get_parcels()

new_parcel_data = {
    "parcel": {
        "name": "John Doe",
        "company_name": "Sendcloud",
        "address": "Insulindelaan 115",
        "house_number": "115",
        "city": "Eindhoven",
        "postal_code": "5642CV",
        "telephone": "+31612345678",
        "request_label": True,
        "email": "john@doe.com",
        "data": [],
        "country": "NL",
        "shipment": {"id": 8,},
        "weight": "10.000",
        "order_number": "1234567890",
        "insured_value": 2000,
    }
}
parcel = Parcels().create_parcel(new_parcel_data)
```

### Develop Mode
For Testing you need to install project in develop mode 
`pip install -e .[develop]` and start this command `python setup.py test`
