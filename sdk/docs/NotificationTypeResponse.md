# NotificationTypeResponse

Holds readonly information about a Finbourne.Notifications.WebApi.Dtos.Notifications.Notification
## Example

```python
from lusid_notifications.models.notification_type_response import NotificationTypeResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with NotificationTypeResponse 

amazon_sqs_notification_type_response_instance = lusid_notifications.models.amazon_sqs_notification_type_response.AmazonSqsNotificationTypeResponse(
                        type = 'AmazonSqs', 
                        api_key_ref = '', 
                        api_secret_ref = '', 
                        body = '', 
                        queue_url_ref = '', )

notification_type_response_instance = NotificationTypeResponse(amazon_sqs_notification_type_response_instance)

```
See all compatible oneOf types with NotificationTypeResponse


 * [AmazonSqsPrincipalAuthNotificationTypeResponse](./AmazonSqsPrincipalAuthNotificationTypeResponse.md)

 * [AzureServiceBusTypeResponse](./AzureServiceBusTypeResponse.md)

 * [EmailNotificationTypeResponse](./EmailNotificationTypeResponse.md)

 * [SmsNotificationTypeResponse](./SmsNotificationTypeResponse.md)

 * [WebhookNotificationTypeResponse](./WebhookNotificationTypeResponse.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

