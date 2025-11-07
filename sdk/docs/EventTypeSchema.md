# EventTypeSchema

An EventType object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the event type | [optional] 
**display_name** | **str** | Identifier name of the event | [optional] 
**description** | **str** | The summary of the event | [optional] 
**application** | **str** | The application associated with the event | [optional] 
**header_schema** | [**List[EventFieldDefinition]**](EventFieldDefinition.md) | The header schema for the event type | [optional] [readonly] 
**body_schema** | [**List[EventFieldDefinition]**](EventFieldDefinition.md) | The body schema for the event type | [optional] [readonly] 
**href** | **str** | A URI for retrieving this schema | [optional] 
## Example

```python
from lusid_notifications.models.event_type_schema import EventTypeSchema
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
application: Optional[StrictStr] = "example_application"
header_schema: Optional[List[EventFieldDefinition]] = # Replace with your value
body_schema: Optional[List[EventFieldDefinition]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
event_type_schema_instance = EventTypeSchema(id=id, display_name=display_name, description=description, application=application, header_schema=header_schema, body_schema=body_schema, href=href)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

