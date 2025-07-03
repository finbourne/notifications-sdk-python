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
from lusid_notifications.models.delivery import Delivery
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

id: StrictStr = "example_id"
event_id: StrictStr = "example_event_id"
subscription_id: ResourceId = # Replace with your value
notification_id: StrictStr = "example_notification_id"
delivery_channel: StrictStr = "example_delivery_channel"
message_details: StrictStr = "example_message_details"
attempts: conlist(Attempt) = # Replace with your value
delivery_instance = Delivery(id=id, event_id=event_id, subscription_id=subscription_id, notification_id=notification_id, delivery_channel=delivery_channel, message_details=message_details, attempts=attempts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

