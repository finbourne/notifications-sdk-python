# lusid_notifications.DeliveriesApi

All URIs are relative to *https://fbn-prd.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_deliveries**](DeliveriesApi.md#list_deliveries) | **GET** /api/deliveries | ListDeliveries: List Deliveries


# **list_deliveries**
> ResourceListOfDelivery list_deliveries(page=page, limit=limit, filter=filter)

ListDeliveries: List Deliveries

Currently only returns deliveries with failed attempts.

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    DeliveriesApi
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
    api_instance = api_client_factory.build(DeliveriesApi)
    page = 'page_example' # str | The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied. (optional)
    limit = 56 # int | The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week's worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be 'AttemptTime gt 2023-08-25' for example (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_deliveries(page=page, limit=limit, filter=filter, opts=opts)

        # ListDeliveries: List Deliveries
        api_response = api_instance.list_deliveries(page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DeliveriesApi->list_deliveries: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied. | [optional] 
 **limit** | **int**| The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week&#39;s worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be &#39;AttemptTime gt 2023-08-25&#39; for example | [optional] 

### Return type

[**ResourceListOfDelivery**](ResourceListOfDelivery.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No deliveries exists with the provided filter(s) |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

