# AttemptStatus

Status of the delivery attempt.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Result of the delivery. | 
**detailed_message** | **str** | The detailed message from attempting to deliver the message. | [optional] 

## Example

```python
from finbourne_notifications.models.attempt_status import AttemptStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AttemptStatus from a JSON string
attempt_status_instance = AttemptStatus.from_json(json)
# print the JSON string representation of the object
print AttemptStatus.to_json()

# convert the object into a dict
attempt_status_dict = attempt_status_instance.to_dict()
# create an instance of AttemptStatus from a dict
attempt_status_form_dict = attempt_status.from_dict(attempt_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


