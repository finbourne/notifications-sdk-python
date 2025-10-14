# WebhookNotificationTypeResponse

Holds readonly information about a Webhook notification
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**http_method** | **str** | The HTTP method such as GET, POST, etc. to use on the request | [optional] 
**url** | **str** | The URL to send the request to | [optional] 
**authentication_type** | **str** | The type of authentication to use on the request | [optional] 
**authentication_configuration_item_paths** | **Dict[str, str]** | The paths of the Configuration Store configuration items that contain the authentication configuration. Each authentication type requires different keys: - Lusid - None required - BasicAuth - Requires &#39;Username&#39; and &#39;Password&#39; - BearerToken - Requires &#39;BearerToken&#39; and optionally &#39;BearerScheme&#39;              e.g. the following would be valid assuming that the config is present in the configuration store at the specified paths:                  \&quot;authenticationType\&quot;: \&quot;BasicAuth\&quot;,     \&quot;authenticationConfigurationItemPaths\&quot;: {         \&quot;Username\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\&quot;,         \&quot;Password\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\&quot;     } | [optional] 
**content_type** | **str** | The type of the content e.g. Json | [optional] 
**content** | **object** | The content of the request | [optional] 
## Example

```python
from lusid_notifications.models.webhook_notification_type_response import WebhookNotificationTypeResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
http_method: Optional[StrictStr] = "example_http_method"
url: Optional[StrictStr] = "example_url"
authentication_type: Optional[StrictStr] = "example_authentication_type"
authentication_configuration_item_paths: Optional[Dict[str, StrictStr]] = # Replace with your value
content_type: Optional[StrictStr] = "example_content_type"
content: Optional[Any] = # Replace with your value
webhook_notification_type_response_instance = WebhookNotificationTypeResponse(type=type, http_method=http_method, url=url, authentication_type=authentication_type, authentication_configuration_item_paths=authentication_configuration_item_paths, content_type=content_type, content=content)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

