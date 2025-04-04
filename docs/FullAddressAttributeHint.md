# FullAddressAttributeHint

A hint that the data contains a full Address contained in a single attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**FullAddressAttributeHintAttribute**](FullAddressAttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.full_address_attribute_hint import FullAddressAttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of FullAddressAttributeHint from a JSON string
full_address_attribute_hint_instance = FullAddressAttributeHint.from_json(json)
# print the JSON string representation of the object
print(FullAddressAttributeHint.to_json())

# convert the object into a dict
full_address_attribute_hint_dict = full_address_attribute_hint_instance.to_dict()
# create an instance of FullAddressAttributeHint from a dict
full_address_attribute_hint_from_dict = FullAddressAttributeHint.from_dict(full_address_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


