# ResourceListOfNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Notification]**](Notification.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_notifications.models.resource_list_of_notification import ResourceListOfNotification

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfNotification from a JSON string
resource_list_of_notification_instance = ResourceListOfNotification.from_json(json)
# print the JSON string representation of the object
print ResourceListOfNotification.to_json()

# convert the object into a dict
resource_list_of_notification_dict = resource_list_of_notification_instance.to_dict()
# create an instance of ResourceListOfNotification from a dict
resource_list_of_notification_form_dict = resource_list_of_notification.from_dict(resource_list_of_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


