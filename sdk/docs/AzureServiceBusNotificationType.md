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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
namespace: StrictStr = "example_namespace"
queue_name: StrictStr = "example_queue_name"
body: StrictStr = "example_body"
tenant_id: StrictStr = "example_tenant_id"
client_id: StrictStr = "example_client_id"
client_secret: StrictStr = "example_client_secret"
azure_service_bus_notification_type_instance = AzureServiceBusNotificationType(type=type, namespace=namespace, queue_name=queue_name, body=body, tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

