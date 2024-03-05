# AmazonSqsPrincipalAuthNotificationTypeResponse

Holds readonly information about an AWS SQS with Principal Authentication notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | [optional] 
**body** | **str** | The body of the Amazon Queue Message | [optional] 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | [optional] 

## Example

```python
from lusid_notifications.models.amazon_sqs_principal_auth_notification_type_response import AmazonSqsPrincipalAuthNotificationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonSqsPrincipalAuthNotificationTypeResponse from a JSON string
amazon_sqs_principal_auth_notification_type_response_instance = AmazonSqsPrincipalAuthNotificationTypeResponse.from_json(json)
# print the JSON string representation of the object
print AmazonSqsPrincipalAuthNotificationTypeResponse.to_json()

# convert the object into a dict
amazon_sqs_principal_auth_notification_type_response_dict = amazon_sqs_principal_auth_notification_type_response_instance.to_dict()
# create an instance of AmazonSqsPrincipalAuthNotificationTypeResponse from a dict
amazon_sqs_principal_auth_notification_type_response_form_dict = amazon_sqs_principal_auth_notification_type_response.from_dict(amazon_sqs_principal_auth_notification_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

