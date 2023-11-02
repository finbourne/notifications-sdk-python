# ManualEventHeader

The header of the manual event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The event type of the manual event | [optional] [readonly] 
**timestamp** | **datetime** | The timestamp of the manual event | [optional] 
**user_id** | **str** | The user ID of the manual event | [optional] 
**request_id** | **str** | The request ID of the manual event | [optional] 

## Example

```python
from finbourne_notifications.models.manual_event_header import ManualEventHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ManualEventHeader from a JSON string
manual_event_header_instance = ManualEventHeader.from_json(json)
# print the JSON string representation of the object
print ManualEventHeader.to_json()

# convert the object into a dict
manual_event_header_dict = manual_event_header_instance.to_dict()
# create an instance of ManualEventHeader from a dict
manual_event_header_form_dict = manual_event_header.from_dict(manual_event_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


