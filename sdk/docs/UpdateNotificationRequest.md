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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
notification_type: NotificationType = # Replace with your value
update_notification_request_instance = UpdateNotificationRequest(display_name=display_name, description=description, notification_type=notification_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

