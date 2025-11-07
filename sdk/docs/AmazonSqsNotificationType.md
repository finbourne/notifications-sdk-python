# AmazonSqsNotificationType

The information required to create or update an AWS SQS notification
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**api_key_ref** | **str** | Reference to API key from Configuration Store | 
**api_secret_ref** | **str** | Reference to API secret from Configuration Store | 
**body** | **str** | The body of the Amazon Queue Message | 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | 
## Example

```python
from lusid_notifications.models.amazon_sqs_notification_type import AmazonSqsNotificationType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
api_key_ref: StrictStr = "example_api_key_ref"
api_secret_ref: StrictStr = "example_api_secret_ref"
body: StrictStr = "example_body"
queue_url_ref: StrictStr = "example_queue_url_ref"
amazon_sqs_notification_type_instance = AmazonSqsNotificationType(type=type, api_key_ref=api_key_ref, api_secret_ref=api_secret_ref, body=body, queue_url_ref=queue_url_ref)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

