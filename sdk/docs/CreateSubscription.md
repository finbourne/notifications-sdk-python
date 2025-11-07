# CreateSubscription

The information required to create a subscription
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the subscription | 
**description** | **str** | The summary of the services provided by the subscription | [optional] 
**status** | **str** | The current status of the subscription. Possible values are: Active, Inactive | 
**matching_pattern** | [**MatchingPattern**](MatchingPattern.md) |  | 
**use_as_auth** | **str** | Id of user associated with subscription. All events associated with  the subscription will use this user to check entitlements against  the resource to send a notification. Can be null, in which case  we&#39;ll default to that of the user making this request | [optional] 
## Example

```python
from lusid_notifications.models.create_subscription import CreateSubscription
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
status: StrictStr = "example_status"
matching_pattern: MatchingPattern = # Replace with your value
use_as_auth: Optional[StrictStr] = "example_use_as_auth"
create_subscription_instance = CreateSubscription(id=id, display_name=display_name, description=description, status=status, matching_pattern=matching_pattern, use_as_auth=use_as_auth)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

