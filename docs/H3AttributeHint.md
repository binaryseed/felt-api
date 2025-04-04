# H3AttributeHint

A hint that the data contains H3 attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**H3AttributeHintAttribute**](H3AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.h3_attribute_hint import H3AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of H3AttributeHint from a JSON string
h3_attribute_hint_instance = H3AttributeHint.from_json(json)
# print the JSON string representation of the object
print(H3AttributeHint.to_json())

# convert the object into a dict
h3_attribute_hint_dict = h3_attribute_hint_instance.to_dict()
# create an instance of H3AttributeHint from a dict
h3_attribute_hint_from_dict = H3AttributeHint.from_dict(h3_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


