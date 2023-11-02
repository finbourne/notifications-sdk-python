# EmailNotificationType

The information required to create or update an Email notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**subject** | **str** | The subject of the email | 
**plain_text_body** | **str** | The plain text body of the email | 
**html_body** | **str** | The HTML body of the email (if any) | [optional] 
**email_address_to** | **List[str]** | &#39;To&#39; recipients of the email | 
**email_address_cc** | **List[str]** | &#39;Cc&#39; recipients of the email | [optional] 
**email_address_bcc** | **List[str]** | &#39;Bcc&#39; recipients of the email | [optional] 

## Example

```python
from finbourne_notifications.models.email_notification_type import EmailNotificationType

# TODO update the JSON string below
json = "{}"
# create an instance of EmailNotificationType from a JSON string
email_notification_type_instance = EmailNotificationType.from_json(json)
# print the JSON string representation of the object
print EmailNotificationType.to_json()

# convert the object into a dict
email_notification_type_dict = email_notification_type_instance.to_dict()
# create an instance of EmailNotificationType from a dict
email_notification_type_form_dict = email_notification_type.from_dict(email_notification_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


