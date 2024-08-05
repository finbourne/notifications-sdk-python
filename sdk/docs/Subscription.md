# Subscription

A subscription object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the subscription | 
**description** | **str** | The summary of the services provided by the subscription | [optional] 
**status** | **str** | The current status of the subscription | 
**matching_pattern** | [**MatchingPattern**](MatchingPattern.md) |  | 
**created_at** | **datetime** | The time at which the subscription was made | 
**user_id_created** | **str** | The user who made the subscription | 
**modified_at** | **datetime** | The time at which the subscription was last modified | 
**user_id_modified** | **str** | The user who last modified the subscription | 
**use_as_auth** | **str** | The user to use as auth for the subscription | 
**href** | **str** | A URI for retrieving this subscription | [optional] 

## Example

```python
from lusid_notifications.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print Subscription.to_json()

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_form_dict = subscription.from_dict(subscription_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


