# Attempt

Details of an attempt of delivery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_number** | **int** | The attempt number of the delivery. | 
**attempt_time** | **datetime** | The time that the delivery was attempted. | 
**status** | [**AttemptStatus**](AttemptStatus.md) |  | 

## Example

```python
from finbourne_notifications.models.attempt import Attempt

# TODO update the JSON string below
json = "{}"
# create an instance of Attempt from a JSON string
attempt_instance = Attempt.from_json(json)
# print the JSON string representation of the object
print Attempt.to_json()

# convert the object into a dict
attempt_dict = attempt_instance.to_dict()
# create an instance of Attempt from a dict
attempt_form_dict = attempt.from_dict(attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


