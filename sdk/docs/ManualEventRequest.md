# ManualEventRequest

The information required to trigger a manual event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**ManualEventBody**](ManualEventBody.md) |  | 

## Example

```python
from lusid_notifications.models.manual_event_request import ManualEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManualEventRequest from a JSON string
manual_event_request_instance = ManualEventRequest.from_json(json)
# print the JSON string representation of the object
print ManualEventRequest.to_json()

# convert the object into a dict
manual_event_request_dict = manual_event_request_instance.to_dict()
# create an instance of ManualEventRequest from a dict
manual_event_request_form_dict = manual_event_request.from_dict(manual_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


