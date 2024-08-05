# Notification

A notification object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **str** | The identifier of the notification | 
**display_name** | **str** | The name of the notification | 
**description** | **str** | The summary of the services provided by the notification | [optional] 
**notification_type** | [**NotificationTypeResponse**](NotificationTypeResponse.md) |  | 
**created_at** | **datetime** | The time at which the subscription was made | 
**user_id_created** | **str** | The user who made the subscription | 
**modified_at** | **datetime** | The time at which the subscription was last modified | 
**user_id_modified** | **str** | The user who last modified the subscription | 
**href** | **str** | A URI for retrieving this notification | [optional] 

## Example

```python
from lusid_notifications.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print Notification.to_json()

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_form_dict = notification.from_dict(notification_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


