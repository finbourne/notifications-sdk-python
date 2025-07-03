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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

notification_id: StrictStr = "example_notification_id"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
notification_type: NotificationType = # Replace with your value
create_notification_request_instance = CreateNotificationRequest(notification_id=notification_id, display_name=display_name, description=description, notification_type=notification_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

