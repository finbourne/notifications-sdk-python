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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
namespace_ref: Optional[StrictStr] = "example_namespace_ref"
queue_name_ref: Optional[StrictStr] = "example_queue_name_ref"
body: Optional[StrictStr] = "example_body"
tenant_id_ref: Optional[StrictStr] = "example_tenant_id_ref"
client_id_ref: Optional[StrictStr] = "example_client_id_ref"
client_secret_ref: Optional[StrictStr] = "example_client_secret_ref"
azure_service_bus_type_response_instance = AzureServiceBusTypeResponse(type=type, namespace_ref=namespace_ref, queue_name_ref=queue_name_ref, body=body, tenant_id_ref=tenant_id_ref, client_id_ref=client_id_ref, client_secret_ref=client_secret_ref)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

