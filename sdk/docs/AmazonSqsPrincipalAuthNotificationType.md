# AmazonSqsPrincipalAuthNotificationType

The information required to create or update an AWS SQS notification with principal authentication
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**body** | **str** | The body of the Amazon Queue Message | 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | 
## Example

```python
from lusid_notifications.models.amazon_sqs_principal_auth_notification_type import AmazonSqsPrincipalAuthNotificationType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
body: StrictStr = "example_body"
queue_url_ref: StrictStr = "example_queue_url_ref"
amazon_sqs_principal_auth_notification_type_instance = AmazonSqsPrincipalAuthNotificationType(type=type, body=body, queue_url_ref=queue_url_ref)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

