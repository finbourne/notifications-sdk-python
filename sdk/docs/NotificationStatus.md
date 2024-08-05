# NotificationStatus

The status object of a notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | The status of the notification | [optional] 
**last_updated** | **datetime** | The time at which the notification status was last updated | [optional] 

## Example

```python
from lusid_notifications.models.notification_status import NotificationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationStatus from a JSON string
notification_status_instance = NotificationStatus.from_json(json)
# print the JSON string representation of the object
print NotificationStatus.to_json()

# convert the object into a dict
notification_status_dict = notification_status_instance.to_dict()
# create an instance of NotificationStatus from a dict
notification_status_form_dict = notification_status.from_dict(notification_status_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


