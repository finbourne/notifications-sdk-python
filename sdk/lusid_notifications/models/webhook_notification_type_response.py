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

class WebhookNotificationTypeResponse(BaseModel):
    """
    Holds readonly information about a Webhook notification  # noqa: E501
    """
    type:  Optional[StrictStr] = Field(None,alias="type", description="The type of delivery mechanism for this notification") 
    http_method:  Optional[StrictStr] = Field(None,alias="httpMethod", description="The HTTP method such as GET, POST, etc. to use on the request") 
    url:  Optional[StrictStr] = Field(None,alias="url", description="The URL to send the request to") 
    authentication_type:  Optional[StrictStr] = Field(None,alias="authenticationType", description="The type of authentication to use on the request") 
    authentication_configuration_item_paths: Optional[Dict[str, StrictStr]] = Field(None, alias="authenticationConfigurationItemPaths", description="The paths of the Configuration Store configuration items that contain the authentication configuration. Each  authentication type requires different keys:  - Lusid - None required  - BasicAuth - Requires 'Username' and 'Password'  - BearerToken - Requires 'BearerToken' and optionally 'BearerScheme'                e.g. the following would be valid assuming that the config is present in the configuration store at the  specified paths:                    \"authenticationType\": \"BasicAuth\",      \"authenticationConfigurationItemPaths\": {          \"Username\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\",          \"Password\": \"config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\"      }")
    content_type:  Optional[StrictStr] = Field(None,alias="contentType", description="The type of the content e.g. Json") 
    content: Optional[Any] = Field(None, description="The content of the request")
    __properties = ["type", "httpMethod", "url", "authenticationType", "authenticationConfigurationItemPaths", "contentType", "content"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Webhook'):
            raise ValueError("must be one of enum values ('Webhook')")
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
    def from_json(cls, json_str: str) -> WebhookNotificationTypeResponse:
        """Create an instance of WebhookNotificationTypeResponse from a JSON string"""
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

        # set to None if http_method (nullable) is None
        # and __fields_set__ contains the field
        if self.http_method is None and "http_method" in self.__fields_set__:
            _dict['httpMethod'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if authentication_type (nullable) is None
        # and __fields_set__ contains the field
        if self.authentication_type is None and "authentication_type" in self.__fields_set__:
            _dict['authenticationType'] = None

        # set to None if authentication_configuration_item_paths (nullable) is None
        # and __fields_set__ contains the field
        if self.authentication_configuration_item_paths is None and "authentication_configuration_item_paths" in self.__fields_set__:
            _dict['authenticationConfigurationItemPaths'] = None

        # set to None if content_type (nullable) is None
        # and __fields_set__ contains the field
        if self.content_type is None and "content_type" in self.__fields_set__:
            _dict['contentType'] = None

        # set to None if content (nullable) is None
        # and __fields_set__ contains the field
        if self.content is None and "content" in self.__fields_set__:
            _dict['content'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebhookNotificationTypeResponse:
        """Create an instance of WebhookNotificationTypeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebhookNotificationTypeResponse.parse_obj(obj)

        _obj = WebhookNotificationTypeResponse.parse_obj({
            "type": obj.get("type"),
            "http_method": obj.get("httpMethod"),
            "url": obj.get("url"),
            "authentication_type": obj.get("authenticationType"),
            "authentication_configuration_item_paths": obj.get("authenticationConfigurationItemPaths"),
            "content_type": obj.get("contentType"),
            "content": obj.get("content")
        })
        return _obj
