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


from typing import Any, Dict
from pydantic.v1 import BaseModel, Field
from lusid_notifications.models.manual_event_body import ManualEventBody

class ManualEventRequest(BaseModel):
    """
    The information required to trigger a manual event  # noqa: E501
    """
    body: ManualEventBody = Field(...)
    __properties = ["body"]

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
    def from_json(cls, json_str: str) -> ManualEventRequest:
        """Create an instance of ManualEventRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of body
        if self.body:
            _dict['body'] = self.body.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManualEventRequest:
        """Create an instance of ManualEventRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ManualEventRequest.parse_obj(obj)

        _obj = ManualEventRequest.parse_obj({
            "body": ManualEventBody.from_dict(obj.get("body")) if obj.get("body") is not None else None
        })
        return _obj
