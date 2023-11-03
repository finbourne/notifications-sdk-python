# ResourceListOfDelivery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Delivery]**](Delivery.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_notifications.models.resource_list_of_delivery import ResourceListOfDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfDelivery from a JSON string
resource_list_of_delivery_instance = ResourceListOfDelivery.from_json(json)
# print the JSON string representation of the object
print ResourceListOfDelivery.to_json()

# convert the object into a dict
resource_list_of_delivery_dict = resource_list_of_delivery_instance.to_dict()
# create an instance of ResourceListOfDelivery from a dict
resource_list_of_delivery_form_dict = resource_list_of_delivery.from_dict(resource_list_of_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


