# MatchingPattern

A matching pattern object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The type of event to subscribe to. The list of available event types can be discovered  by calling the ‘List available EventTypes’ API endpoint. | 
**filter** | **str** | A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched | [optional] 
## Example

```python
from lusid_notifications.models.matching_pattern import MatchingPattern
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

event_type: StrictStr = "example_event_type"
filter: Optional[StrictStr] = "example_filter"
matching_pattern_instance = MatchingPattern(event_type=event_type, filter=filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

