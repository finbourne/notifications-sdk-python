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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator
from lusid_notifications.models.notification_type_response import NotificationTypeResponse

class Notification(BaseModel):
    """
    A notification object  # noqa: E501
    """
    notification_id: constr(strict=True, min_length=1) = Field(..., alias="notificationId", description="The identifier of the notification")
    display_name: constr(strict=True, max_length=64, min_length=0) = Field(..., alias="displayName", description="The name of the notification")
    description: Optional[constr(strict=True, max_length=512, min_length=1)] = Field(None, description="The summary of the services provided by the notification")
    notification_type: NotificationTypeResponse = Field(..., alias="notificationType")
    created_at: datetime = Field(..., alias="createdAt", description="The time at which the subscription was made")
    user_id_created: constr(strict=True, min_length=1) = Field(..., alias="userIdCreated", description="The user who made the subscription")
    modified_at: datetime = Field(..., alias="modifiedAt", description="The time at which the subscription was last modified")
    user_id_modified: constr(strict=True, min_length=1) = Field(..., alias="userIdModified", description="The user who last modified the subscription")
    href: Optional[StrictStr] = Field(None, description="A URI for retrieving this notification")
    __properties = ["notificationId", "displayName", "description", "notificationType", "createdAt", "userIdCreated", "modifiedAt", "userIdModified", "href"]

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
    def from_json(cls, json_str: str) -> Notification:
        """Create an instance of Notification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of notification_type
        if self.notification_type:
            _dict['notificationType'] = self.notification_type.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Notification:
        """Create an instance of Notification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Notification.parse_obj(obj)

        _obj = Notification.parse_obj({
            "notification_id": obj.get("notificationId"),
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "notification_type": NotificationTypeResponse.from_dict(obj.get("notificationType")) if obj.get("notificationType") is not None else None,
            "created_at": obj.get("createdAt"),
            "user_id_created": obj.get("userIdCreated"),
            "modified_at": obj.get("modifiedAt"),
            "user_id_modified": obj.get("userIdModified"),
            "href": obj.get("href")
        })
        return _obj
