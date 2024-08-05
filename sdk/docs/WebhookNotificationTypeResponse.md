# WebhookNotificationTypeResponse

Holds readonly information about a Webhook notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**http_method** | **str** | The HTTP method such as GET, POST, etc. to use on the request | [optional] 
**url** | **str** | The URL to send the request to | [optional] 
**authentication_type** | **str** | The type of authentication to use on the request | [optional] 
**authentication_configuration_item_paths** | **Dict[str, str]** | The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires &#39;Username&#39; and &#39;Password&#39;  - BearerToken - Requires &#39;BearerToken&#39; and optionally &#39;BearerScheme&#39;                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \&quot;authenticationType\&quot;: \&quot;BasicAuth\&quot;,      \&quot;authenticationConfigurationItemPaths\&quot;: {          \&quot;Username\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\&quot;,          \&quot;Password\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\&quot;      } | [optional] 
**content_type** | **str** | The type of the content e.g. Json | [optional] 
**content** | **object** | The content of the request | [optional] 

## Example

```python
from lusid_notifications.models.webhook_notification_type_response import WebhookNotificationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookNotificationTypeResponse from a JSON string
webhook_notification_type_response_instance = WebhookNotificationTypeResponse.from_json(json)
# print the JSON string representation of the object
print WebhookNotificationTypeResponse.to_json()

# convert the object into a dict
webhook_notification_type_response_dict = webhook_notification_type_response_instance.to_dict()
# create an instance of WebhookNotificationTypeResponse from a dict
webhook_notification_type_response_form_dict = webhook_notification_type_response.from_dict(webhook_notification_type_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


