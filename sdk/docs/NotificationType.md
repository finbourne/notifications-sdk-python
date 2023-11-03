# NotificationType

Holds information about a Finbourne.Notifications.WebApi.Dtos.Notifications.Notification that is being created

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**api_key_ref** | **str** | Reference to API key from Configuration Store | 
**api_secret_ref** | **str** | Reference to API secret from Configuration Store | 
**body** | **str** | The body of the SMS | 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | 
**subject** | **str** | The subject of the email | 
**plain_text_body** | **str** | The plain text body of the email | 
**html_body** | **str** | The HTML body of the email (if any) | [optional] 
**email_address_to** | **List[str]** | &#39;To&#39; recipients of the email | 
**email_address_cc** | **List[str]** | &#39;Cc&#39; recipients of the email | [optional] 
**email_address_bcc** | **List[str]** | &#39;Bcc&#39; recipients of the email | [optional] 
**recipients** | **List[str]** | The phone numbers to which the SMS will be sent to (E.164 format) | 
**http_method** | **str** | The HTTP method such as GET, POST, etc. to use on the request | 
**url** | **str** | The URL to send the request to | 
**authentication_type** | **str** | The type of authentication to use on the request, can be one of the following values:  - Lusid -  Internal LUSID call  - BasicAuth - User specified Username and password  - BearerToken - Authorization header with Bearer scheme and user specified key  - None - No Authorization required on the webhook call | 
**authentication_configuration_item_paths** | **Dict[str, str]** | The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires &#39;Username&#39; and &#39;Password&#39;  - BearerToken - Requires &#39;BearerToken&#39; and optionally &#39;BearerScheme&#39;  - None - None required                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \&quot;authenticationType\&quot;: \&quot;BasicAuth\&quot;,      \&quot;authenticationConfigurationItemPaths\&quot;: {          \&quot;Username\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\&quot;,          \&quot;Password\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\&quot;      } | [optional] 
**content_type** | **str** | The type of the content e.g. Json | 
**content** | **object** | The content of the request | [optional] 

## Example

```python
from lusid_notifications.models.notification_type import NotificationType

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationType from a JSON string
notification_type_instance = NotificationType.from_json(json)
# print the JSON string representation of the object
print NotificationType.to_json()

# convert the object into a dict
notification_type_dict = notification_type_instance.to_dict()
# create an instance of NotificationType from a dict
notification_type_form_dict = notification_type.from_dict(notification_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


