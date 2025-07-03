# EmailNotificationType

The information required to create or update an Email notification
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**subject** | **str** | The subject of the email | 
**plain_text_body** | **str** | The plain text body of the email | 
**html_body** | **str** | The HTML body of the email (if any) | [optional] 
**email_address_to** | **List[str]** | &#39;To&#39; recipients of the email | 
**email_address_cc** | **List[str]** | &#39;Cc&#39; recipients of the email | [optional] 
**email_address_bcc** | **List[str]** | &#39;Bcc&#39; recipients of the email | [optional] 
## Example

```python
from lusid_notifications.models.email_notification_type import EmailNotificationType
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

type: StrictStr = "example_type"
subject: StrictStr = "example_subject"
plain_text_body: StrictStr = "example_plain_text_body"
html_body: Optional[StrictStr] = "example_html_body"
email_address_to: conlist(StrictStr, max_items=10, min_items=1) = Field(..., alias="emailAddressTo", description="'To' recipients of the email")
email_address_cc: Optional[conlist(StrictStr, max_items=10, min_items=0)] = Field(None, alias="emailAddressCc", description="'Cc' recipients of the email")
email_address_bcc: Optional[conlist(StrictStr, max_items=10, min_items=0)] = Field(None, alias="emailAddressBcc", description="'Bcc' recipients of the email")
email_notification_type_instance = EmailNotificationType(type=type, subject=subject, plain_text_body=plain_text_body, html_body=html_body, email_address_to=email_address_to, email_address_cc=email_address_cc, email_address_bcc=email_address_bcc)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

