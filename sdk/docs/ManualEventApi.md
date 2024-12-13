# lusid_notifications.ManualEventApi

All URIs are relative to *https://fbn-prd.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_manual_event**](ManualEventApi.md#trigger_manual_event) | **POST** /api/manualevent | TriggerManualEvent: Trigger a manual event.


# **trigger_manual_event**
> ManualEvent trigger_manual_event(manual_event_request)

TriggerManualEvent: Trigger a manual event.

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    ManualEventApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "notificationsUrl":"https://<your-domain>.lusid.com/notification",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid_notifications SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ManualEventApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # manual_event_request = ManualEventRequest.from_json("")
    # manual_event_request = ManualEventRequest.from_dict({})
    manual_event_request = ManualEventRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.trigger_manual_event(manual_event_request, opts=opts)

        # TriggerManualEvent: Trigger a manual event.
        api_response = api_instance.trigger_manual_event(manual_event_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ManualEventApi->trigger_manual_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_event_request** | [**ManualEventRequest**](ManualEventRequest.md)| The data required to trigger a manual event. | 

### Return type

[**ManualEvent**](ManualEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

