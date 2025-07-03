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
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

type: StrictStr = "example_type"
body: StrictStr = "example_body"
recipients: conlist(StrictStr, max_items=10, min_items=1) = Field(..., description="The phone numbers to which the SMS will be sent to (E.164 format)")
sms_notification_type_instance = SmsNotificationType(type=type, body=body, recipients=recipients)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

