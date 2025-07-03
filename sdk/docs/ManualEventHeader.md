# ManualEventHeader

The header of the manual event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The event type of the manual event | [optional] [readonly] 
**timestamp** | **datetime** | The timestamp of the manual event | [optional] 
**user_id** | **str** | The user ID of the manual event | [optional] 
**request_id** | **str** | The request ID of the manual event | [optional] 
## Example

```python
from lusid_notifications.models.manual_event_header import ManualEventHeader
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from datetime import datetime
event_type: Optional[StrictStr] = "example_event_type"
timestamp: Optional[datetime] = # Replace with your value
user_id: Optional[StrictStr] = "example_user_id"
request_id: Optional[StrictStr] = "example_request_id"
manual_event_header_instance = ManualEventHeader(event_type=event_type, timestamp=timestamp, user_id=user_id, request_id=request_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

