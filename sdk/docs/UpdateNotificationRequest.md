# UpdateNotificationRequest

The information required to update a notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the notification | 
**description** | **str** | The summary of the services provided by the notification | [optional] 
**notification_type** | [**NotificationType**](NotificationType.md) |  | 

## Example

```python
from lusid_notifications.models.update_notification_request import UpdateNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationRequest from a JSON string
update_notification_request_instance = UpdateNotificationRequest.from_json(json)
# print the JSON string representation of the object
print UpdateNotificationRequest.to_json()

# convert the object into a dict
update_notification_request_dict = update_notification_request_instance.to_dict()
# create an instance of UpdateNotificationRequest from a dict
update_notification_request_form_dict = update_notification_request.from_dict(update_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


