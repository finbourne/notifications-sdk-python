# ResourceListOfSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Subscription]**](Subscription.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_notifications.models.resource_list_of_subscription import ResourceListOfSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfSubscription from a JSON string
resource_list_of_subscription_instance = ResourceListOfSubscription.from_json(json)
# print the JSON string representation of the object
print ResourceListOfSubscription.to_json()

# convert the object into a dict
resource_list_of_subscription_dict = resource_list_of_subscription_instance.to_dict()
# create an instance of ResourceListOfSubscription from a dict
resource_list_of_subscription_form_dict = resource_list_of_subscription.from_dict(resource_list_of_subscription_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


