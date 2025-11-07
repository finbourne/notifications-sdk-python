# EventFieldDefinition

An EventFieldDefinition object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the field | [optional] 
**type** | **str** | Type of the field | [optional] 
## Example

```python
from lusid_notifications.models.event_field_definition import EventFieldDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: Optional[StrictStr] = "example_name"
type: Optional[StrictStr] = "example_type"
event_field_definition_instance = EventFieldDefinition(name=name, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

