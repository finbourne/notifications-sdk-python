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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, constr, validator 

class AzureServiceBusNotificationType(BaseModel):
    """
    The information required to create or update an Azure Service Bus notification  # noqa: E501
    """
    type:  StrictStr = Field(...,alias="type", description="The type of delivery mechanism for this notification") 
    namespace:  StrictStr = Field(...,alias="namespace", description="Reference to namespace from Configuration Store") 
    queue_name:  StrictStr = Field(...,alias="queueName", description="Reference to queue name from Configuration Store") 
    body:  StrictStr = Field(...,alias="body", description="The body of the Azure Service Bus Message") 
    tenant_id:  StrictStr = Field(...,alias="tenantId", description="Reference to tenant id from Configuration Store") 
    client_id:  StrictStr = Field(...,alias="clientId", description="Reference to client id from Configuration Store") 
    client_secret:  StrictStr = Field(...,alias="clientSecret", description="Reference to client secret from Configuration Store") 
    __properties = ["type", "namespace", "queueName", "body", "tenantId", "clientId", "clientSecret"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'AzureServiceBusNotificationType' not in [ 
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

        if value not in ('AzureServiceBus'):
            raise ValueError("must be one of enum values ('AzureServiceBus')")
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
    def from_json(cls, json_str: str) -> AzureServiceBusNotificationType:
        """Create an instance of AzureServiceBusNotificationType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureServiceBusNotificationType:
        """Create an instance of AzureServiceBusNotificationType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureServiceBusNotificationType.parse_obj(obj)

        _obj = AzureServiceBusNotificationType.parse_obj({
            "type": obj.get("type"),
            "namespace": obj.get("namespace"),
            "queue_name": obj.get("queueName"),
            "body": obj.get("body"),
            "tenant_id": obj.get("tenantId"),
            "client_id": obj.get("clientId"),
            "client_secret": obj.get("clientSecret")
        })
        return _obj
