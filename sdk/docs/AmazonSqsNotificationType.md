# AmazonSqsNotificationType

The information required to create or update an AWS SQS notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of delivery mechanism for this notification | 
**api_key_ref** | **str** | Reference to API key from Configuration Store | 
**api_secret_ref** | **str** | Reference to API secret from Configuration Store | 
**body** | **str** | The body of the Amazon Queue Message | 
**queue_url_ref** | **str** | Reference to queue url from Configuration Store | 

## Example

```python
from lusid_notifications.models.amazon_sqs_notification_type import AmazonSqsNotificationType

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonSqsNotificationType from a JSON string
amazon_sqs_notification_type_instance = AmazonSqsNotificationType.from_json(json)
# print the JSON string representation of the object
print AmazonSqsNotificationType.to_json()

# convert the object into a dict
amazon_sqs_notification_type_dict = amazon_sqs_notification_type_instance.to_dict()
# create an instance of AmazonSqsNotificationType from a dict
amazon_sqs_notification_type_form_dict = amazon_sqs_notification_type.from_dict(amazon_sqs_notification_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


