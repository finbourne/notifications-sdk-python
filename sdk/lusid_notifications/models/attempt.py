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

from datetime import datetime
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt
from lusid_notifications.models.attempt_status import AttemptStatus

class Attempt(BaseModel):
    """
    Details of an attempt of delivery.  # noqa: E501
    """
    attempt_number: StrictInt = Field(..., alias="attemptNumber", description="The attempt number of the delivery.")
    attempt_time: datetime = Field(..., alias="attemptTime", description="The time that the delivery was attempted.")
    status: AttemptStatus = Field(...)
    __properties = ["attemptNumber", "attemptTime", "status"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Attempt:
        """Create an instance of Attempt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Attempt:
        """Create an instance of Attempt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Attempt.parse_obj(obj)

        _obj = Attempt.parse_obj({
            "attempt_number": obj.get("attemptNumber"),
            "attempt_time": obj.get("attemptTime"),
            "status": AttemptStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None
        })
        return _obj
