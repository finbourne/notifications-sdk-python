# ResourceListOfEventTypeSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[EventTypeSchema]**](EventTypeSchema.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_notifications.models.resource_list_of_event_type_schema import ResourceListOfEventTypeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfEventTypeSchema from a JSON string
resource_list_of_event_type_schema_instance = ResourceListOfEventTypeSchema.from_json(json)
# print the JSON string representation of the object
print ResourceListOfEventTypeSchema.to_json()

# convert the object into a dict
resource_list_of_event_type_schema_dict = resource_list_of_event_type_schema_instance.to_dict()
# create an instance of ResourceListOfEventTypeSchema from a dict
resource_list_of_event_type_schema_form_dict = resource_list_of_event_type_schema.from_dict(resource_list_of_event_type_schema_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


