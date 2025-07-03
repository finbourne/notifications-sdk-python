# EmailNotificationTypeResponse

Holds readonly information about an Email notification
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**subject** | **str** | The subject of the email | [optional] 
**plain_text_body** | **str** | The plain text body of the email | [optional] 
**html_body** | **str** | The HTML body of the email (if any) | [optional] 
**email_address_to** | **List[str]** | &#39;To&#39; recipients of the email | [optional] 
**email_address_cc** | **List[str]** | &#39;Cc&#39; recipients of the email | [optional] 
**email_address_bcc** | **List[str]** | &#39;Bcc&#39; recipients of the email | [optional] 
## Example

```python
from lusid_notifications.models.email_notification_type_response import EmailNotificationTypeResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, validator

type: Optional[StrictStr] = "example_type"
subject: Optional[StrictStr] = "example_subject"
plain_text_body: Optional[StrictStr] = "example_plain_text_body"
html_body: Optional[StrictStr] = "example_html_body"
email_address_to: Optional[conlist(StrictStr)] = # Replace with your value
email_address_cc: Optional[conlist(StrictStr)] = # Replace with your value
email_address_bcc: Optional[conlist(StrictStr)] = # Replace with your value
email_notification_type_response_instance = EmailNotificationTypeResponse(type=type, subject=subject, plain_text_body=plain_text_body, html_body=html_body, email_address_to=email_address_to, email_address_cc=email_address_cc, email_address_bcc=email_address_bcc)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

