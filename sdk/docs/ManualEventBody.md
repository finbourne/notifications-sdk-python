# ManualEventBody

The body of the manual event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The subject of the manual event | 
**message** | **str** | The message of the manual event | 
**json_message** | **object** | The JSON message of the manual event | [optional] 
## Example

```python
from lusid_notifications.models.manual_event_body import ManualEventBody
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

subject: StrictStr = "example_subject"
message: StrictStr = "example_message"
json_message: Optional[Any] = # Replace with your value
manual_event_body_instance = ManualEventBody(subject=subject, message=message, json_message=json_message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

