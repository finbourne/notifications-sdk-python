# lusid_notifications.DeliveriesApi

All URIs are relative to *https://fbn-ci.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_deliveries**](DeliveriesApi.md#list_deliveries) | **GET** /api/deliveries | [EXPERIMENTAL] ListDeliveries: List Deliveries


# **list_deliveries**
> ResourceListOfDelivery list_deliveries(page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListDeliveries: List Deliveries

Currently only returns deliveries with failed attempts.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_notifications
from lusid_notifications.rest import ApiException
from lusid_notifications.models.resource_list_of_delivery import ResourceListOfDelivery
from pprint import pprint

from lusid_notifications import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid_notifications ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/notification"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid_notifications.DeliveriesApi)
    page = 'page_example' # str | The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied. (optional)
    limit = 56 # int | The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week's worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be 'AttemptTime gt 2023-08-25' for example (optional)

    try:
        # [EXPERIMENTAL] ListDeliveries: List Deliveries
        api_response = await api_instance.list_deliveries(page=page, limit=limit, filter=filter)
        print("The response of DeliveriesApi->list_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesApi->list_deliveries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied. | [optional] 
 **limit** | **int**| The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week&#39;s worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be &#39;AttemptTime gt 2023-08-25&#39; for example | [optional] 

### Return type

[**ResourceListOfDelivery**](ResourceListOfDelivery.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No deliveries exists with the provided filter(s) |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

