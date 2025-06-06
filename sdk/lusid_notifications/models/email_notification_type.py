# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist, constr, validator 

class EmailNotificationType(BaseModel):
    """
    The information required to create or update an Email notification  # noqa: E501
    """
    type:  StrictStr = Field(...,alias="type", description="The type of delivery mechanism for this notification") 
    subject:  StrictStr = Field(...,alias="subject", description="The subject of the email") 
    plain_text_body:  StrictStr = Field(...,alias="plainTextBody", description="The plain text body of the email") 
    html_body:  Optional[StrictStr] = Field(None,alias="htmlBody", description="The HTML body of the email (if any)") 
    email_address_to: conlist(StrictStr) = Field(..., alias="emailAddressTo", description="'To' recipients of the email")
    email_address_cc: Optional[conlist(StrictStr)] = Field(None, alias="emailAddressCc", description="'Cc' recipients of the email")
    email_address_bcc: Optional[conlist(StrictStr)] = Field(None, alias="emailAddressBcc", description="'Bcc' recipients of the email")
    __properties = ["type", "subject", "plainTextBody", "htmlBody", "emailAddressTo", "emailAddressCc", "emailAddressBcc"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'EmailNotificationType' not in [ 
                                    # For notification application classes
                                    'AmazonSqsNotificationType',
                                    'AmazonSqsNotificationTypeResponse',
                                    'AmazonSqsPrincipalAuthNotificationType',
                                    'AmazonSqsPrincipalAuthNotificationTypeResponse',
                                    'AzureServiceBusTypeResponse',
                                    'AzureServiceBusNotificationType',
                                    'EmailNotificationType',
                                    'EmailNotificationTypeResponse',
                                    'SmsNotificationType',
                                    'SmsNotificationTypeResponse',
                                    'WebhookNotificationType',
                                    'WebhookNotificationTypeResponse',
                        
                                    # For workflow application classes
                                    'CreateChildTasksAction', 
                                    'RunWorkerAction', 
                                    'TriggerParentTaskAction',
                                    'CreateChildTasksActionResponse', 
                                    'RunWorkerActionResponse',
                                    'TriggerParentTaskActionResponse',
                                    'CreateNewTaskActivity',
                                    'UpdateMatchingTasksActivity',
                                    'CreateNewTaskActivityResponse', 
                                    'UpdateMatchingTasksActivityResponse',
                                    'Fail', 
                                    'GroupReconciliation', 
                                    'HealthCheck', 
                                    'LuminesceView', 
                                    'SchedulerJob', 
                                    'Sleep',
                                    'FailResponse', 
                                    'GroupReconciliationResponse', 
                                    'HealthCheckResponse', 
                                    'LuminesceViewResponse', 
                                    'SchedulerJobResponse', 
                                    'SleepResponse']:
           return value
        
        # Only validate the 'type' property of the class
        if "type" != "type":
            return value

        if value not in ('Email'):
            raise ValueError("must be one of enum values ('Email')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EmailNotificationType:
        """Create an instance of EmailNotificationType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if html_body (nullable) is None
        # and __fields_set__ contains the field
        if self.html_body is None and "html_body" in self.__fields_set__:
            _dict['htmlBody'] = None

        # set to None if email_address_cc (nullable) is None
        # and __fields_set__ contains the field
        if self.email_address_cc is None and "email_address_cc" in self.__fields_set__:
            _dict['emailAddressCc'] = None

        # set to None if email_address_bcc (nullable) is None
        # and __fields_set__ contains the field
        if self.email_address_bcc is None and "email_address_bcc" in self.__fields_set__:
            _dict['emailAddressBcc'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EmailNotificationType:
        """Create an instance of EmailNotificationType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EmailNotificationType.parse_obj(obj)

        _obj = EmailNotificationType.parse_obj({
            "type": obj.get("type"),
            "subject": obj.get("subject"),
            "plain_text_body": obj.get("plainTextBody"),
            "html_body": obj.get("htmlBody"),
            "email_address_to": obj.get("emailAddressTo"),
            "email_address_cc": obj.get("emailAddressCc"),
            "email_address_bcc": obj.get("emailAddressBcc")
        })
        return _obj
