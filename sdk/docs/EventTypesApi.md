# lusid_notifications.EventTypesApi

All URIs are relative to *https://fbn-prd.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_type**](EventTypesApi.md#get_event_type) | **GET** /api/eventtypes/{eventType} | GetEventType: Gets the specified event type schema.
[**list_event_types**](EventTypesApi.md#list_event_types) | **GET** /api/eventtypes | ListEventTypes: Lists all of the available event types.


# **get_event_type**
> EventTypeSchema get_event_type(event_type)

GetEventType: Gets the specified event type schema.

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    EventTypesApi
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
    api_instance = api_client_factory.build(EventTypesApi)
    event_type = 'event_type_example' # str | The event type to retrieve schema for.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_event_type(event_type, opts=opts)

        # GetEventType: Gets the specified event type schema.
        api_response = api_instance.get_event_type(event_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EventTypesApi->get_event_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**| The event type to retrieve schema for. | 

### Return type

[**EventTypeSchema**](EventTypeSchema.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No event type exists with the specified type |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_event_types**
> ResourceListOfEventTypeSchema list_event_types()

ListEventTypes: Lists all of the available event types.

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    EventTypesApi
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
    api_instance = api_client_factory.build(EventTypesApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_event_types(opts=opts)

        # ListEventTypes: Lists all of the available event types.
        api_response = api_instance.list_event_types()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EventTypesApi->list_event_types: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfEventTypeSchema**](ResourceListOfEventTypeSchema.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No event types found |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

