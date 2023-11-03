# lusid_notifications.ManualEventApi

All URIs are relative to *https://fbn-ci.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_manual_event**](ManualEventApi.md#trigger_manual_event) | **POST** /api/manualevent | [EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.


# **trigger_manual_event**
> ManualEvent trigger_manual_event(manual_event_request)

[EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid_notifications
from lusid_notifications.rest import ApiException
from lusid_notifications.models.manual_event import ManualEvent
from lusid_notifications.models.manual_event_request import ManualEventRequest
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
    api_instance = api_client_factory.build(lusid_notifications.ManualEventApi)
    manual_event_request = {"Body":{"subject":"TestSubject","message":"TestMessage","jsonMessage":{"TestField1":"TestValue1","TestField2":"TestValue2"}}} # ManualEventRequest | The data required to trigger a manual event.

    try:
        # [EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.
        api_response = await api_instance.trigger_manual_event(manual_event_request)
        print("The response of ManualEventApi->trigger_manual_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualEventApi->trigger_manual_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_event_request** | [**ManualEventRequest**](ManualEventRequest.md)| The data required to trigger a manual event. | 

### Return type

[**ManualEvent**](ManualEvent.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

