# CreateNotificationRequest

The information required to create a notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **str** | The identifier of the notification. | 
**display_name** | **str** | The name of the notification | 
**description** | **str** | The summary of the services provided by the notification | [optional] 
**notification_type** | [**NotificationType**](NotificationType.md) |  | 

## Example

```python
from lusid_notifications.models.create_notification_request import CreateNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationRequest from a JSON string
create_notification_request_instance = CreateNotificationRequest.from_json(json)
# print the JSON string representation of the object
print CreateNotificationRequest.to_json()

# convert the object into a dict
create_notification_request_dict = create_notification_request_instance.to_dict()
# create an instance of CreateNotificationRequest from a dict
create_notification_request_form_dict = create_notification_request.from_dict(create_notification_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


