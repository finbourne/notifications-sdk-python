# ManualEvent

Details of a manually triggered event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**ManualEventHeader**](ManualEventHeader.md) |  | 
**body** | [**ManualEventBody**](ManualEventBody.md) |  | 
## Example

```python
from lusid_notifications.models.manual_event import ManualEvent
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

header: ManualEventHeader = # Replace with your value
body: ManualEventBody = # Replace with your value
manual_event_instance = ManualEvent(header=header, body=body)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

