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


from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, validator 

class AmazonSqsPrincipalAuthNotificationTypeResponse(BaseModel):
    """
    Holds readonly information about an AWS SQS with Principal Authentication notification  # noqa: E501
    """
    type:  Optional[StrictStr] = Field(None,alias="type", description="The type of delivery mechanism for this notification") 
    body:  Optional[StrictStr] = Field(None,alias="body", description="The body of the Amazon Queue Message") 
    queue_url_ref:  Optional[StrictStr] = Field(None,alias="queueUrlRef", description="Reference to queue url from Configuration Store") 
    __properties = ["type", "body", "queueUrlRef"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if not value == 'AmazonSqsPrincipalAuth':
            raise ValueError("must be one of enum values ('AmazonSqsPrincipalAuth')")
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
    def from_json(cls, json_str: str) -> AmazonSqsPrincipalAuthNotificationTypeResponse:
        """Create an instance of AmazonSqsPrincipalAuthNotificationTypeResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if body (nullable) is None
        # and __fields_set__ contains the field
        if self.body is None and "body" in self.__fields_set__:
            _dict['body'] = None

        # set to None if queue_url_ref (nullable) is None
        # and __fields_set__ contains the field
        if self.queue_url_ref is None and "queue_url_ref" in self.__fields_set__:
            _dict['queueUrlRef'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AmazonSqsPrincipalAuthNotificationTypeResponse:
        """Create an instance of AmazonSqsPrincipalAuthNotificationTypeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AmazonSqsPrincipalAuthNotificationTypeResponse.parse_obj(obj)

        _obj = AmazonSqsPrincipalAuthNotificationTypeResponse.parse_obj({
            "type": obj.get("type"),
            "body": obj.get("body"),
            "queue_url_ref": obj.get("queueUrlRef")
        })
        return _obj
