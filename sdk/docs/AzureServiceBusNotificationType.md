# AzureServiceBusNotificationType

The information required to create or update an Azure Service Bus notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**namespace** | **str** | Reference to namespace from Configuration Store | 
**queue_name** | **str** | Reference to queue name from Configuration Store | 
**body** | **str** | The body of the Azure Service Bus Message | 
**tenant_id** | **str** | Reference to tenant id from Configuration Store | 
**client_id** | **str** | Reference to client id from Configuration Store | 
**client_secret** | **str** | Reference to client secret from Configuration Store | 

## Example

```python
from lusid_notifications.models.azure_service_bus_notification_type import AzureServiceBusNotificationType

# TODO update the JSON string below
json = "{}"
# create an instance of AzureServiceBusNotificationType from a JSON string
azure_service_bus_notification_type_instance = AzureServiceBusNotificationType.from_json(json)
# print the JSON string representation of the object
print AzureServiceBusNotificationType.to_json()

# convert the object into a dict
azure_service_bus_notification_type_dict = azure_service_bus_notification_type_instance.to_dict()
# create an instance of AzureServiceBusNotificationType from a dict
azure_service_bus_notification_type_form_dict = azure_service_bus_notification_type.from_dict(azure_service_bus_notification_type_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


