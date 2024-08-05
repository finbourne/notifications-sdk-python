# SmsNotificationTypeResponse

Holds readonly information about an SMS notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**body** | **str** | The body of the SMS | [optional] 
**recipients** | **List[str]** | The phone numbers to which the SMS will be sent to (E.164 format) | [optional] 

## Example

```python
from lusid_notifications.models.sms_notification_type_response import SmsNotificationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmsNotificationTypeResponse from a JSON string
sms_notification_type_response_instance = SmsNotificationTypeResponse.from_json(json)
# print the JSON string representation of the object
print SmsNotificationTypeResponse.to_json()

# convert the object into a dict
sms_notification_type_response_dict = sms_notification_type_response_instance.to_dict()
# create an instance of SmsNotificationTypeResponse from a dict
sms_notification_type_response_form_dict = sms_notification_type_response.from_dict(sms_notification_type_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


