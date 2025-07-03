# ManualEventRequest

The information required to trigger a manual event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**ManualEventBody**](ManualEventBody.md) |  | 
## Example

```python
from lusid_notifications.models.manual_event_request import ManualEventRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

body: ManualEventBody = # Replace with your value
manual_event_request_instance = ManualEventRequest(body=body)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

