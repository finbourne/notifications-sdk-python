# NotificationTypeResponse

Holds readonly information about a Finbourne.Notifications.WebApi.Dtos.Notifications.Notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**api_key_ref** | **str** | Reference to API key from Configuration Store | [optional] 
**api_secret_ref** | **str** | Reference to API secret from Configuration Store | [optional] 
**body** | **str** | The body of the SMS | [optional] 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | [optional] 
**subject** | **str** | The subject of the email | [optional] 
**plain_text_body** | **str** | The plain text body of the email | [optional] 
**html_body** | **str** | The HTML body of the email (if any) | [optional] 
**email_address_to** | **List[str]** | &#39;To&#39; recipients of the email | [optional] 
**email_address_cc** | **List[str]** | &#39;Cc&#39; recipients of the email | [optional] 
**email_address_bcc** | **List[str]** | &#39;Bcc&#39; recipients of the email | [optional] 
**recipients** | **List[str]** | The phone numbers to which the SMS will be sent to (E.164 format) | [optional] 
**http_method** | **str** | The HTTP method such as GET, POST, etc. to use on the request | [optional] 
**url** | **str** | The URL to send the request to | [optional] 
**authentication_type** | **str** | The type of authentication to use on the request | [optional] 
**authentication_configuration_item_paths** | **Dict[str, str]** | The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires &#39;Username&#39; and &#39;Password&#39;  - BearerToken - Requires &#39;BearerToken&#39; and optionally &#39;BearerScheme&#39;                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \&quot;authenticationType\&quot;: \&quot;BasicAuth\&quot;,      \&quot;authenticationConfigurationItemPaths\&quot;: {          \&quot;Username\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\&quot;,          \&quot;Password\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\&quot;      } | [optional] 
**content_type** | **str** | The type of the content e.g. Json | [optional] 
**content** | **object** | The content of the request | [optional] 

## Example

```python
from lusid_notifications.models.notification_type_response import NotificationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTypeResponse from a JSON string
notification_type_response_instance = NotificationTypeResponse.from_json(json)
# print the JSON string representation of the object
print NotificationTypeResponse.to_json()

# convert the object into a dict
notification_type_response_dict = notification_type_response_instance.to_dict()
# create an instance of NotificationTypeResponse from a dict
notification_type_response_form_dict = notification_type_response.from_dict(notification_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


