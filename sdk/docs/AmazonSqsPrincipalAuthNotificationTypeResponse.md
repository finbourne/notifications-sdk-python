# AmazonSqsPrincipalAuthNotificationTypeResponse

Holds readonly information about an AWS SQS with Principal Authentication notification
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**body** | **str** | The body of the Amazon Queue Message | [optional] 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | [optional] 
## Example

```python
from lusid_notifications.models.amazon_sqs_principal_auth_notification_type_response import AmazonSqsPrincipalAuthNotificationTypeResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
body: Optional[StrictStr] = "example_body"
queue_url_ref: Optional[StrictStr] = "example_queue_url_ref"
amazon_sqs_principal_auth_notification_type_response_instance = AmazonSqsPrincipalAuthNotificationTypeResponse(type=type, body=body, queue_url_ref=queue_url_ref)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

