# SmsNotificationType

The information required to create or update an SMS notification
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**body** | **str** | The body of the SMS | 
**recipients** | **List[str]** | The phone numbers to which the SMS will be sent to (E.164 format) | 
## Example

```python
from lusid_notifications.models.sms_notification_type import SmsNotificationType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
body: StrictStr = "example_body"
recipients: List[StrictStr] = # Replace with your value
sms_notification_type_instance = SmsNotificationType(type=type, body=body, recipients=recipients)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

