# NotificationType

Holds information about a Finbourne.Notifications.WebApi.Dtos.Notifications.Notification that is being created
## Example

```python
from lusid_notifications.models.notification_type import NotificationType
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with NotificationType 

amazon_sqs_notification_type_instance = lusid_notifications.models.amazon_sqs_notification_type.AmazonSqsNotificationType(
                        type = 'AmazonSqs', 
                        api_key_ref = '0', 
                        api_secret_ref = '0', 
                        body = ' Aa6w77ikCX*cKCmv|`K/V0', 
                        queue_url_ref = '0', )

notification_type_instance = NotificationType(amazon_sqs_notification_type_instance)

```
See all compatible oneOf types with NotificationType


 * [AmazonSqsPrincipalAuthNotificationType](./AmazonSqsPrincipalAuthNotificationType.md)

 * [AzureServiceBusNotificationType](./AzureServiceBusNotificationType.md)

 * [EmailNotificationType](./EmailNotificationType.md)

 * [SmsNotificationType](./SmsNotificationType.md)

 * [WebhookNotificationType](./WebhookNotificationType.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

