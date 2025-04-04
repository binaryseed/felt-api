# USState2020AttributeHint

A hint that the data contains a US State (Census 2020) attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**USState2020AttributeHintAttribute**](USState2020AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.us_state2020_attribute_hint import USState2020AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of USState2020AttributeHint from a JSON string
us_state2020_attribute_hint_instance = USState2020AttributeHint.from_json(json)
# print the JSON string representation of the object
print(USState2020AttributeHint.to_json())

# convert the object into a dict
us_state2020_attribute_hint_dict = us_state2020_attribute_hint_instance.to_dict()
# create an instance of USState2020AttributeHint from a dict
us_state2020_attribute_hint_from_dict = USState2020AttributeHint.from_dict(us_state2020_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


