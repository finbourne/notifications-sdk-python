# lusid_notifications.SubscriptionsApi

All URIs are relative to *https://fbn-prd.lusid.com/notification*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /api/subscriptions | [EXPERIMENTAL] CreateSubscription: Create a new subscription.
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /api/subscriptions/{scope}/{code} | [EXPERIMENTAL] DeleteSubscription: Delete a subscription.
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /api/subscriptions/{scope}/{code} | [EXPERIMENTAL] GetSubscription: Get a subscription.
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /api/subscriptions | [EXPERIMENTAL] ListSubscriptions: List subscriptions.
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PUT** /api/subscriptions/{scope}/{code} | [EXPERIMENTAL] UpdateSubscription: Update an existing subscription.


# **create_subscription**
> Subscription create_subscription(create_subscription)

[EXPERIMENTAL] CreateSubscription: Create a new subscription.

### Example

```python
import asyncio
from lusid_notifications.exceptions import ApiException
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    ApiClientFactory,
    SubscriptionsApi
)

async def main():

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

    # Use the lusid_notifications ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SubscriptionsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_subscription = CreateSubscription()
        # create_subscription = CreateSubscription.from_json("")
        create_subscription = CreateSubscription.from_dict({"id":{"scope":"TestScope","code":"TestCode"},"displayName":"TestDisplayName","description":"TestDescription","status":"Active","matchingPattern":{"eventType":"Manual","filter":"Body.Message eq 'TestMessage'"},"useAsAuth":"TestClient"}) # CreateSubscription | The data to create a subscription

        try:
            # [EXPERIMENTAL] CreateSubscription: Create a new subscription.
            api_response = await api_instance.create_subscription(create_subscription)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription** | [**CreateSubscription**](CreateSubscription.md)| The data to create a subscription | 

### Return type

[**Subscription**](Subscription.md)

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

# **delete_subscription**
> delete_subscription(scope, code)

[EXPERIMENTAL] DeleteSubscription: Delete a subscription.

### Example

```python
import asyncio
from lusid_notifications.exceptions import ApiException
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    ApiClientFactory,
    SubscriptionsApi
)

async def main():

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

    # Use the lusid_notifications ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SubscriptionsApi)
        scope = 'scope_example' # str | The scope that identifies a subscription
        code = 'code_example' # str | The code that identifies a subscription

        try:
            # [EXPERIMENTAL] DeleteSubscription: Delete a subscription.
            await api_instance.delete_subscription(scope, code)        except ApiException as e:
            print("Exception when calling SubscriptionsApi->delete_subscription: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 

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
**404** | No subscription exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_subscription**
> Subscription get_subscription(scope, code)

[EXPERIMENTAL] GetSubscription: Get a subscription.

### Example

```python
import asyncio
from lusid_notifications.exceptions import ApiException
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    ApiClientFactory,
    SubscriptionsApi
)

async def main():

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

    # Use the lusid_notifications ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SubscriptionsApi)
        scope = 'scope_example' # str | The scope that identifies a subscription
        code = 'code_example' # str | The code that identifies a subscription

        try:
            # [EXPERIMENTAL] GetSubscription: Get a subscription.
            api_response = await api_instance.get_subscription(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 

### Return type

[**Subscription**](Subscription.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No subscription exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_subscriptions**
> ResourceListOfSubscription list_subscriptions(filter=filter, sort_by=sort_by, page=page, limit=limit)

[EXPERIMENTAL] ListSubscriptions: List subscriptions.

### Example

```python
import asyncio
from lusid_notifications.exceptions import ApiException
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    ApiClientFactory,
    SubscriptionsApi
)

async def main():

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

    # Use the lusid_notifications ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SubscriptionsApi)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about <a href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</a>. (optional)
        sort_by = 'sort_by_example' # str | Fields to order the result set. Read more about <a href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</a> (optional)
        page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied the filter  field should not be supplied. (optional)
        limit = 56 # int | The maximum number of subscriptions to retrieve. (optional)

        try:
            # [EXPERIMENTAL] ListSubscriptions: List subscriptions.
            api_response = await api_instance.list_subscriptions(filter=filter, sort_by=sort_by, page=page, limit=limit)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SubscriptionsApi->list_subscriptions: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about &lt;a href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/a&gt;. | [optional] 
 **sort_by** | **str**| Fields to order the result set. Read more about &lt;a href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/a&gt; | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied the filter  field should not be supplied. | [optional] 
 **limit** | **int**| The maximum number of subscriptions to retrieve. | [optional] 

### Return type

[**ResourceListOfSubscription**](ResourceListOfSubscription.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_subscription**
> Subscription update_subscription(scope, code, update_subscription)

[EXPERIMENTAL] UpdateSubscription: Update an existing subscription.

### Example

```python
import asyncio
from lusid_notifications.exceptions import ApiException
from lusid_notifications.models import *
from pprint import pprint
from lusid_notifications import (
    ApiClientFactory,
    SubscriptionsApi
)

async def main():

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

    # Use the lusid_notifications ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SubscriptionsApi)
        scope = 'scope_example' # str | The scope that identifies a subscription
        code = 'code_example' # str | The code that identifies a subscription

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_subscription = UpdateSubscription()
        # update_subscription = UpdateSubscription.from_json("")
        update_subscription = UpdateSubscription.from_dict({"displayName":"TestDisplayName","description":"TestDescription","status":"Active","matchingPattern":{"eventType":"Manual","filter":"Body.Message eq 'TestMessage'"},"useAsAuth":"TestClient"}) # UpdateSubscription | The data to update a subscription

        try:
            # [EXPERIMENTAL] UpdateSubscription: Update an existing subscription.
            api_response = await api_instance.update_subscription(scope, code, update_subscription)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SubscriptionsApi->update_subscription: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | 
 **code** | **str**| The code that identifies a subscription | 
 **update_subscription** | [**UpdateSubscription**](UpdateSubscription.md)| The data to update a subscription | 

### Return type

[**Subscription**](Subscription.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No subscription exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

