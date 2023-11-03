# UpdateSubscription

The information required to update a subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the subscription | 
**description** | **str** | The summary of the services provided by the subscription | [optional] 
**status** | **str** | The current status of the subscription. Possible values are: Active, Inactive | 
**matching_pattern** | [**MatchingPattern**](MatchingPattern.md) |  | 
**use_as_auth** | **str** | Id of user associated with subscription. All events associated with   the subscription will use this user to check entitlements against   the resource to send a notification. Can be null, in which case   we&#39;ll default to that of the user making this request | [optional] 

## Example

```python
from lusid_notifications.models.update_subscription import UpdateSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscription from a JSON string
update_subscription_instance = UpdateSubscription.from_json(json)
# print the JSON string representation of the object
print UpdateSubscription.to_json()

# convert the object into a dict
update_subscription_dict = update_subscription_instance.to_dict()
# create an instance of UpdateSubscription from a dict
update_subscription_form_dict = update_subscription.from_dict(update_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


