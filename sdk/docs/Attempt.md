# Attempt

Details of an attempt of delivery.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_number** | **int** | The attempt number of the delivery. | 
**attempt_time** | **datetime** | The time that the delivery was attempted. | 
**status** | [**AttemptStatus**](AttemptStatus.md) |  | 
## Example

```python
from lusid_notifications.models.attempt import Attempt
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt
from datetime import datetime
attempt_number: StrictInt = # Replace with your value
attempt_number: StrictInt = 42
attempt_time: datetime = # Replace with your value
status: AttemptStatus = # Replace with your value
attempt_instance = Attempt(attempt_number=attempt_number, attempt_time=attempt_time, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

