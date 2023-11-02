# SmsNotificationType

The information required to create or update an SMS notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**body** | **str** | The body of the SMS | 
**recipients** | **List[str]** | The phone numbers to which the SMS will be sent to (E.164 format) | 

## Example

```python
from finbourne_notifications.models.sms_notification_type import SmsNotificationType

# TODO update the JSON string below
json = "{}"
# create an instance of SmsNotificationType from a JSON string
sms_notification_type_instance = SmsNotificationType.from_json(json)
# print the JSON string representation of the object
print SmsNotificationType.to_json()

# convert the object into a dict
sms_notification_type_dict = sms_notification_type_instance.to_dict()
# create an instance of SmsNotificationType from a dict
sms_notification_type_form_dict = sms_notification_type.from_dict(sms_notification_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


