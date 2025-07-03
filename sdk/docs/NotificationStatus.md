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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from datetime import datetime
result: Optional[StrictStr] = "example_result"
last_updated: Optional[datetime] = # Replace with your value
notification_status_instance = NotificationStatus(result=result, last_updated=last_updated)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

