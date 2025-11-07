# NotificationType

Holds information about a Finbourne.Notifications.WebApi.Dtos.Notifications.Notification that is being created
## Example

```python
from lusid_notifications.models.notification_type import NotificationType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with NotificationType 

amazon_sqs_notification_type_instance = lusid_notifications.models.amazon_sqs_notification_type.AmazonSqsNotificationType(
                        type = 'AmazonSqs', 
                        api_key_ref = '', 
                        api_secret_ref = '', 
                        body = ' Aa6w77ikCX*cKCmv|`K/V', 
                        queue_url_ref = '', )

notification_type_instance = NotificationType(amazon_sqs_notification_type_instance)

```
See all compatible oneOf types with NotificationType


 * [AmazonSqsPrincipalAuthNotificationType](./AmazonSqsPrincipalAuthNotificationType.md)

 * [AzureServiceBusNotificationType](./AzureServiceBusNotificationType.md)

 * [EmailNotificationType](./EmailNotificationType.md)

 * [SmsNotificationType](./SmsNotificationType.md)

 * [WebhookNotificationType](./WebhookNotificationType.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

