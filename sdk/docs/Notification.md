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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

notification_id: StrictStr = "example_notification_id"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
notification_type: NotificationTypeResponse = # Replace with your value
created_at: datetime = # Replace with your value
user_id_created: StrictStr = "example_user_id_created"
modified_at: datetime = # Replace with your value
user_id_modified: StrictStr = "example_user_id_modified"
href: Optional[StrictStr] = "example_href"
notification_instance = Notification(notification_id=notification_id, display_name=display_name, description=description, notification_type=notification_type, created_at=created_at, user_id_created=user_id_created, modified_at=modified_at, user_id_modified=user_id_modified, href=href)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

