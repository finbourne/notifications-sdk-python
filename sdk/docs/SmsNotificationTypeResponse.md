# SmsNotificationTypeResponse

Holds readonly information about an SMS notification
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**body** | **str** | The body of the SMS | [optional] 
**recipients** | **List[str]** | The phone numbers to which the SMS will be sent to (E.164 format) | [optional] 
## Example

```python
from lusid_notifications.models.sms_notification_type_response import SmsNotificationTypeResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
body: Optional[StrictStr] = "example_body"
recipients: Optional[List[StrictStr]] = # Replace with your value
sms_notification_type_response_instance = SmsNotificationTypeResponse(type=type, body=body, recipients=recipients)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

