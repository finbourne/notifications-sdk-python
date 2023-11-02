# Delivery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the delivery. | 
**event_id** | **str** | The identifier of the associated event. | 
**subscription_id** | [**ResourceId**](ResourceId.md) |  | 
**notification_id** | **str** | The identifier of the associated notification. | 
**delivery_channel** | **str** | The delivery channel of the message. | 
**message_details** | **str** | The Details of the delivery message as JSON string. | 
**attempts** | [**List[Attempt]**](Attempt.md) | A list of all the delivery attempts made for this message. | 

## Example

```python
from finbourne_notifications.models.delivery import Delivery

# TODO update the JSON string below
json = "{}"
# create an instance of Delivery from a JSON string
delivery_instance = Delivery.from_json(json)
# print the JSON string representation of the object
print Delivery.to_json()

# convert the object into a dict
delivery_dict = delivery_instance.to_dict()
# create an instance of Delivery from a dict
delivery_form_dict = delivery.from_dict(delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


