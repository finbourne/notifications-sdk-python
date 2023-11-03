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

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypeSchema from a JSON string
event_type_schema_instance = EventTypeSchema.from_json(json)
# print the JSON string representation of the object
print EventTypeSchema.to_json()

# convert the object into a dict
event_type_schema_dict = event_type_schema_instance.to_dict()
# create an instance of EventTypeSchema from a dict
event_type_schema_form_dict = event_type_schema.from_dict(event_type_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


