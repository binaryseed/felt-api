# WKTWKBLiteralAttributeHint

A hint that the data contains a WKT/WKB Literal attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**WKTWKBLiteralAttributeHintAttribute**](WKTWKBLiteralAttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.wktwkb_literal_attribute_hint import WKTWKBLiteralAttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of WKTWKBLiteralAttributeHint from a JSON string
wktwkb_literal_attribute_hint_instance = WKTWKBLiteralAttributeHint.from_json(json)
# print the JSON string representation of the object
print(WKTWKBLiteralAttributeHint.to_json())

# convert the object into a dict
wktwkb_literal_attribute_hint_dict = wktwkb_literal_attribute_hint_instance.to_dict()
# create an instance of WKTWKBLiteralAttributeHint from a dict
wktwkb_literal_attribute_hint_from_dict = WKTWKBLiteralAttributeHint.from_dict(wktwkb_literal_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


