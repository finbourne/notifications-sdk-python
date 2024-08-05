# AmazonSqsPrincipalAuthNotificationType

The information required to create or update an AWS SQS notification with principal authentication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**body** | **str** | The body of the Amazon Queue Message | 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | 

## Example

```python
from lusid_notifications.models.amazon_sqs_principal_auth_notification_type import AmazonSqsPrincipalAuthNotificationType

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonSqsPrincipalAuthNotificationType from a JSON string
amazon_sqs_principal_auth_notification_type_instance = AmazonSqsPrincipalAuthNotificationType.from_json(json)
# print the JSON string representation of the object
print AmazonSqsPrincipalAuthNotificationType.to_json()

# convert the object into a dict
amazon_sqs_principal_auth_notification_type_dict = amazon_sqs_principal_auth_notification_type_instance.to_dict()
# create an instance of AmazonSqsPrincipalAuthNotificationType from a dict
amazon_sqs_principal_auth_notification_type_form_dict = amazon_sqs_principal_auth_notification_type.from_dict(amazon_sqs_principal_auth_notification_type_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


