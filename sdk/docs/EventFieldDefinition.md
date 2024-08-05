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

# TODO update the JSON string below
json = "{}"
# create an instance of EventFieldDefinition from a JSON string
event_field_definition_instance = EventFieldDefinition.from_json(json)
# print the JSON string representation of the object
print EventFieldDefinition.to_json()

# convert the object into a dict
event_field_definition_dict = event_field_definition_instance.to_dict()
# create an instance of EventFieldDefinition from a dict
event_field_definition_form_dict = event_field_definition.from_dict(event_field_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


