# AzureServiceBusTypeResponse

Holds readonly information about an Azure Service Bus notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**namespace_ref** | **str** | Reference to namespace from Configuration Store | [optional] 
**queue_name_ref** | **str** | Reference to queue name from Configuration Store | [optional] 
**body** | **str** | The body of the Azure service bus Message | [optional] 
**tenant_id_ref** | **str** | Reference to tenant id  from Configuration Store | [optional] 
**client_id_ref** | **str** | Reference to client id from Configuration Store | [optional] 
**client_secret_ref** | **str** | Reference to client secret from Configuration Store | [optional] 

## Example

```python
from lusid_notifications.models.azure_service_bus_type_response import AzureServiceBusTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AzureServiceBusTypeResponse from a JSON string
azure_service_bus_type_response_instance = AzureServiceBusTypeResponse.from_json(json)
# print the JSON string representation of the object
print AzureServiceBusTypeResponse.to_json()

# convert the object into a dict
azure_service_bus_type_response_dict = azure_service_bus_type_response_instance.to_dict()
# create an instance of AzureServiceBusTypeResponse from a dict
azure_service_bus_type_response_form_dict = azure_service_bus_type_response.from_dict(azure_service_bus_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


