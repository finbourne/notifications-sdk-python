# ManualEventBody

The body of the manual event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The subject of the manual event | 
**message** | **str** | The message of the manual event | 
**json_message** | **object** | The JSON message of the manual event | [optional] 

## Example

```python
from lusid_notifications.models.manual_event_body import ManualEventBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManualEventBody from a JSON string
manual_event_body_instance = ManualEventBody.from_json(json)
# print the JSON string representation of the object
print ManualEventBody.to_json()

# convert the object into a dict
manual_event_body_dict = manual_event_body_instance.to_dict()
# create an instance of ManualEventBody from a dict
manual_event_body_form_dict = manual_event_body.from_dict(manual_event_body_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


