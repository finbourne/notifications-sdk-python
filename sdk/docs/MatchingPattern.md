# MatchingPattern

A matching pattern object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The type of event to subscribe to. The list of available event types can be discovered  by calling the ‘List available EventTypes’ API endpoint. | 
**filter** | **str** | A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched | [optional] 

## Example

```python
from lusid_notifications.models.matching_pattern import MatchingPattern

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingPattern from a JSON string
matching_pattern_instance = MatchingPattern.from_json(json)
# print the JSON string representation of the object
print MatchingPattern.to_json()

# convert the object into a dict
matching_pattern_dict = matching_pattern_instance.to_dict()
# create an instance of MatchingPattern from a dict
matching_pattern_form_dict = matching_pattern.from_dict(matching_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


