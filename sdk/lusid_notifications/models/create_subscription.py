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
from pydantic.v1 import BaseModel, Field, constr, validator
from lusid_notifications.models.matching_pattern import MatchingPattern
from lusid_notifications.models.resource_id import ResourceId

class CreateSubscription(BaseModel):
    """
    The information required to create a subscription  # noqa: E501
    """
    id: ResourceId = Field(...)
    display_name: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="displayName", description="The name of the subscription")
    description: Optional[constr(strict=True, max_length=512, min_length=1)] = Field(None, description="The summary of the services provided by the subscription")
    status: constr(strict=True, min_length=1) = Field(..., description="The current status of the subscription. Possible values are: Active, Inactive")
    matching_pattern: MatchingPattern = Field(..., alias="matchingPattern")
    use_as_auth: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="useAsAuth", description="Id of user associated with subscription. All events associated with   the subscription will use this user to check entitlements against   the resource to send a notification. Can be null, in which case   we'll default to that of the user making this request")
    __properties = ["id", "displayName", "description", "status", "matchingPattern", "useAsAuth"]

    @validator('display_name')
    def display_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('use_as_auth')
    def use_as_auth_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

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
    def from_json(cls, json_str: str) -> CreateSubscription:
        """Create an instance of CreateSubscription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of matching_pattern
        if self.matching_pattern:
            _dict['matchingPattern'] = self.matching_pattern.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if use_as_auth (nullable) is None
        # and __fields_set__ contains the field
        if self.use_as_auth is None and "use_as_auth" in self.__fields_set__:
            _dict['useAsAuth'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSubscription:
        """Create an instance of CreateSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSubscription.parse_obj(obj)

        _obj = CreateSubscription.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "matching_pattern": MatchingPattern.from_dict(obj.get("matchingPattern")) if obj.get("matchingPattern") is not None else None,
            "use_as_auth": obj.get("useAsAuth")
        })
        return _obj
