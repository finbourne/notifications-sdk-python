# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator
from lusid_notifications.models.amazon_sqs_notification_type_response import AmazonSqsNotificationTypeResponse
from lusid_notifications.models.amazon_sqs_principal_auth_notification_type_response import AmazonSqsPrincipalAuthNotificationTypeResponse
from lusid_notifications.models.email_notification_type_response import EmailNotificationTypeResponse
from lusid_notifications.models.sms_notification_type_response import SmsNotificationTypeResponse
from lusid_notifications.models.webhook_notification_type_response import WebhookNotificationTypeResponse
from typing import Union, Any, List, TYPE_CHECKING
from pydantic.v1 import StrictStr, Field

NOTIFICATIONTYPERESPONSE_ONE_OF_SCHEMAS = ["AmazonSqsNotificationTypeResponse", "AmazonSqsPrincipalAuthNotificationTypeResponse", "EmailNotificationTypeResponse", "SmsNotificationTypeResponse", "WebhookNotificationTypeResponse"]

class NotificationTypeResponse(BaseModel):
    """
    Holds readonly information about a Finbourne.Notifications.WebApi.Dtos.Notifications.Notification
    """
    # data type: AmazonSqsNotificationTypeResponse
    oneof_schema_1_validator: Optional[AmazonSqsNotificationTypeResponse] = None
    # data type: AmazonSqsPrincipalAuthNotificationTypeResponse
    oneof_schema_2_validator: Optional[AmazonSqsPrincipalAuthNotificationTypeResponse] = None
    # data type: EmailNotificationTypeResponse
    oneof_schema_3_validator: Optional[EmailNotificationTypeResponse] = None
    # data type: SmsNotificationTypeResponse
    oneof_schema_4_validator: Optional[SmsNotificationTypeResponse] = None
    # data type: WebhookNotificationTypeResponse
    oneof_schema_5_validator: Optional[WebhookNotificationTypeResponse] = None
    if TYPE_CHECKING:
        actual_instance: Union[AmazonSqsNotificationTypeResponse, AmazonSqsPrincipalAuthNotificationTypeResponse, EmailNotificationTypeResponse, SmsNotificationTypeResponse, WebhookNotificationTypeResponse]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(NOTIFICATIONTYPERESPONSE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = NotificationTypeResponse.construct()
        error_messages = []
        match = 0
        # validate data type: AmazonSqsNotificationTypeResponse
        if not isinstance(v, AmazonSqsNotificationTypeResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AmazonSqsNotificationTypeResponse`")
        else:
            match += 1
        # validate data type: AmazonSqsPrincipalAuthNotificationTypeResponse
        if not isinstance(v, AmazonSqsPrincipalAuthNotificationTypeResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AmazonSqsPrincipalAuthNotificationTypeResponse`")
        else:
            match += 1
        # validate data type: EmailNotificationTypeResponse
        if not isinstance(v, EmailNotificationTypeResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EmailNotificationTypeResponse`")
        else:
            match += 1
        # validate data type: SmsNotificationTypeResponse
        if not isinstance(v, SmsNotificationTypeResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SmsNotificationTypeResponse`")
        else:
            match += 1
        # validate data type: WebhookNotificationTypeResponse
        if not isinstance(v, WebhookNotificationTypeResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhookNotificationTypeResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in NotificationTypeResponse with oneOf schemas: AmazonSqsNotificationTypeResponse, AmazonSqsPrincipalAuthNotificationTypeResponse, EmailNotificationTypeResponse, SmsNotificationTypeResponse, WebhookNotificationTypeResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in NotificationTypeResponse with oneOf schemas: AmazonSqsNotificationTypeResponse, AmazonSqsPrincipalAuthNotificationTypeResponse, EmailNotificationTypeResponse, SmsNotificationTypeResponse, WebhookNotificationTypeResponse. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> NotificationTypeResponse:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> NotificationTypeResponse:
        """Returns the object represented by the json string"""
        instance = NotificationTypeResponse.construct()
        error_messages = []
        match = 0

        # deserialize data into AmazonSqsNotificationTypeResponse
        try:
            instance.actual_instance = AmazonSqsNotificationTypeResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AmazonSqsPrincipalAuthNotificationTypeResponse
        try:
            instance.actual_instance = AmazonSqsPrincipalAuthNotificationTypeResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EmailNotificationTypeResponse
        try:
            instance.actual_instance = EmailNotificationTypeResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SmsNotificationTypeResponse
        try:
            instance.actual_instance = SmsNotificationTypeResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WebhookNotificationTypeResponse
        try:
            instance.actual_instance = WebhookNotificationTypeResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into NotificationTypeResponse with oneOf schemas: AmazonSqsNotificationTypeResponse, AmazonSqsPrincipalAuthNotificationTypeResponse, EmailNotificationTypeResponse, SmsNotificationTypeResponse, WebhookNotificationTypeResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into NotificationTypeResponse with oneOf schemas: AmazonSqsNotificationTypeResponse, AmazonSqsPrincipalAuthNotificationTypeResponse, EmailNotificationTypeResponse, SmsNotificationTypeResponse, WebhookNotificationTypeResponse. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())
