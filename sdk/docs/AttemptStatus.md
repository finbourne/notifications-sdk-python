# AttemptStatus

Status of the delivery attempt.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Result of the delivery. | 
**detailed_message** | **str** | The detailed message from attempting to deliver the message. | [optional] 
## Example

```python
from lusid_notifications.models.attempt_status import AttemptStatus
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

result: StrictStr = "example_result"
detailed_message: Optional[StrictStr] = "example_detailed_message"
attempt_status_instance = AttemptStatus(result=result, detailed_message=detailed_message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

