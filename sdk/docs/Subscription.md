# Subscription

A subscription object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the subscription | 
**description** | **str** | The summary of the services provided by the subscription | [optional] 
**status** | **str** | The current status of the subscription | 
**matching_pattern** | [**MatchingPattern**](MatchingPattern.md) |  | 
**created_at** | **datetime** | The time at which the subscription was made | 
**user_id_created** | **str** | The user who made the subscription | 
**modified_at** | **datetime** | The time at which the subscription was last modified | 
**user_id_modified** | **str** | The user who last modified the subscription | 
**use_as_auth** | **str** | The user to use as auth for the subscription | 
**href** | **str** | A URI for retrieving this subscription | [optional] 
## Example

```python
from lusid_notifications.models.subscription import Subscription
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
status: StrictStr = "example_status"
matching_pattern: MatchingPattern = # Replace with your value
created_at: datetime = # Replace with your value
user_id_created: StrictStr = "example_user_id_created"
modified_at: datetime = # Replace with your value
user_id_modified: StrictStr = "example_user_id_modified"
use_as_auth: StrictStr = "example_use_as_auth"
href: Optional[StrictStr] = "example_href"
subscription_instance = Subscription(id=id, display_name=display_name, description=description, status=status, matching_pattern=matching_pattern, created_at=created_at, user_id_created=user_id_created, modified_at=modified_at, user_id_modified=user_id_modified, use_as_auth=use_as_auth, href=href)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

