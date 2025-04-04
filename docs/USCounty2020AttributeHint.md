# USCounty2020AttributeHint

A hint that the data contains a US County (Census 2020) attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**USCounty2020AttributeHintAttribute**](USCounty2020AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.us_county2020_attribute_hint import USCounty2020AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of USCounty2020AttributeHint from a JSON string
us_county2020_attribute_hint_instance = USCounty2020AttributeHint.from_json(json)
# print the JSON string representation of the object
print(USCounty2020AttributeHint.to_json())

# convert the object into a dict
us_county2020_attribute_hint_dict = us_county2020_attribute_hint_instance.to_dict()
# create an instance of USCounty2020AttributeHint from a dict
us_county2020_attribute_hint_from_dict = USCounty2020AttributeHint.from_dict(us_county2020_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


