# EmailNotificationTypeResponse

Holds readonly information about an Email notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**subject** | **str** | The subject of the email | [optional] 
**plain_text_body** | **str** | The plain text body of the email | [optional] 
**html_body** | **str** | The HTML body of the email (if any) | [optional] 
**email_address_to** | **List[str]** | &#39;To&#39; recipients of the email | [optional] 
**email_address_cc** | **List[str]** | &#39;Cc&#39; recipients of the email | [optional] 
**email_address_bcc** | **List[str]** | &#39;Bcc&#39; recipients of the email | [optional] 

## Example

```python
from lusid_notifications.models.email_notification_type_response import EmailNotificationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailNotificationTypeResponse from a JSON string
email_notification_type_response_instance = EmailNotificationTypeResponse.from_json(json)
# print the JSON string representation of the object
print EmailNotificationTypeResponse.to_json()

# convert the object into a dict
email_notification_type_response_dict = email_notification_type_response_instance.to_dict()
# create an instance of EmailNotificationTypeResponse from a dict
email_notification_type_response_form_dict = email_notification_type_response.from_dict(email_notification_type_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


