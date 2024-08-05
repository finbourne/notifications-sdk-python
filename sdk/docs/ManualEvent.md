# ManualEvent

Details of a manually triggered event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**ManualEventHeader**](ManualEventHeader.md) |  | 
**body** | [**ManualEventBody**](ManualEventBody.md) |  | 

## Example

```python
from lusid_notifications.models.manual_event import ManualEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ManualEvent from a JSON string
manual_event_instance = ManualEvent.from_json(json)
# print the JSON string representation of the object
print ManualEvent.to_json()

# convert the object into a dict
manual_event_dict = manual_event_instance.to_dict()
# create an instance of ManualEvent from a dict
manual_event_form_dict = manual_event.from_dict(manual_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


