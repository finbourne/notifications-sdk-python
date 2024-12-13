# lusid_notifications.NotificationsApi

All URIs are relative to *https://fbn-prd.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](NotificationsApi.md#create_notification) | **POST** /api/subscriptions/{scope}/{code}/notifications | CreateNotification: Add a Notification to a Subscription.
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /api/subscriptions/{scope}/{code}/notifications/{id} | DeleteNotification: Delete a notification for a given subscription.
[**get_notification**](NotificationsApi.md#get_notification) | **GET** /api/subscriptions/{scope}/{code}/notifications/{id} | GetNotification: Get a notification on a subscription.
[**list_notifications**](NotificationsApi.md#list_notifications) | **GET** /api/subscriptions/{scope}/{code}/notifications | ListNotifications: List all notifications on a subscription.
[**update_notification**](NotificationsApi.md#update_notification) | **PUT** /api/subscriptions/{scope}/{code}/notifications/{id} | UpdateNotification: Update a Notification for a Subscription


# **create_notification**
> Notification create_notification(scope, code, create_notification_request)

CreateNotification: Add a Notification to a Subscription.

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    NotificationsApi
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
    api_instance = api_client_factory.build(NotificationsApi)
    scope = 'scope_example' # str | The scope that identifies a subscription
    code = 'code_example' # str | The code that identifies a subscription

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_notification_request = CreateNotificationRequest.from_json("")
    # create_notification_request = CreateNotificationRequest.from_dict({})
    create_notification_request = CreateNotificationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_notification(scope, code, create_notification_request, opts=opts)

        # CreateNotification: Add a Notification to a Subscription.
        api_response = api_instance.create_notification(scope, code, create_notification_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling NotificationsApi->create_notification: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **create_notification_request** | [**CreateNotificationRequest**](CreateNotificationRequest.md)| The data to create a notification | 

### Return type

[**Notification**](Notification.md)

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

# **delete_notification**
> delete_notification(scope, code, id)

DeleteNotification: Delete a notification for a given subscription.

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    NotificationsApi
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
    api_instance = api_client_factory.build(NotificationsApi)
    scope = 'scope_example' # str | The scope that identifies a subscription
    code = 'code_example' # str | The code that identifies a subscription
    id = 'id_example' # str | The unique identifier of the notification

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_notification(scope, code, id, opts=opts)

        # DeleteNotification: Delete a notification for a given subscription.
        api_instance.delete_notification(scope, code, id)
    except ApiException as e:
        print("Exception when calling NotificationsApi->delete_notification: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_notification**
> Notification get_notification(scope, code, id)

GetNotification: Get a notification on a subscription.

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    NotificationsApi
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
    api_instance = api_client_factory.build(NotificationsApi)
    scope = 'scope_example' # str | The scope that identifies a subscription
    code = 'code_example' # str | The code that identifies a subscription
    id = 'id_example' # str | The unique identifier of the notification

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_notification(scope, code, id, opts=opts)

        # GetNotification: Get a notification on a subscription.
        api_response = api_instance.get_notification(scope, code, id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling NotificationsApi->get_notification: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 

### Return type

[**Notification**](Notification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_notifications**
> ResourceListOfNotification list_notifications(scope, code)

ListNotifications: List all notifications on a subscription.

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    NotificationsApi
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
    api_instance = api_client_factory.build(NotificationsApi)
    scope = 'scope_example' # str | The scope that identifies a subscription
    code = 'code_example' # str | The code that identifies a subscription

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_notifications(scope, code, opts=opts)

        # ListNotifications: List all notifications on a subscription.
        api_response = api_instance.list_notifications(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling NotificationsApi->list_notifications: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 

### Return type

[**ResourceListOfNotification**](ResourceListOfNotification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notifications exists with the provided filter(s) |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_notification**
> Notification update_notification(scope, code, id, update_notification_request)

UpdateNotification: Update a Notification for a Subscription

### Example

```python
from lusid_notifications.exceptions import ApiException
from lusid_notifications.extensions.configuration_options import ConfigurationOptions
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    SyncApiClientFactory,
    NotificationsApi
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
    api_instance = api_client_factory.build(NotificationsApi)
    scope = 'scope_example' # str | The scope that identifies a subscription
    code = 'code_example' # str | The code that identifies a subscription
    id = 'id_example' # str | The unique identifier of the notification

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_notification_request = UpdateNotificationRequest.from_json("")
    # update_notification_request = UpdateNotificationRequest.from_dict({})
    update_notification_request = UpdateNotificationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_notification(scope, code, id, update_notification_request, opts=opts)

        # UpdateNotification: Update a Notification for a Subscription
        api_response = api_instance.update_notification(scope, code, id, update_notification_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling NotificationsApi->update_notification: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **id** | **str**| The unique identifier of the notification | 
 **update_notification_request** | [**UpdateNotificationRequest**](UpdateNotificationRequest.md)| The data to update a notification | 

### Return type

[**Notification**](Notification.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

