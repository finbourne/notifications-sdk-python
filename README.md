![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

# LUSID<sup>®</sup> Notifications Python SDK


| branch | status |
| --- | --- |
| `main` |  ![PyPI](https://img.shields.io/pypi/v/lusid-notifications-sdk?color=blue)

## Installation

The PyPi package for the LUSID Notifications SDK can installed using the following:

```
$ pip install lusid-notifications-sdk finbourne-sdk-utilities
```

## Usage

```
import lusid_notifications
from fbnsdkutilities import ApiClientFactory

api_factory = ApiClientFactory(lusid_notifications, api_secrets_filename="secrets.json")
event_types_api = api_factory.build(lusid_notifications.api.EventTypesApi)

response = event_types_api.list_event_types().values
print(response)
```
