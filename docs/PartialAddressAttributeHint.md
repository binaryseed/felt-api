# PartialAddressAttributeHint

A hint that the data contains an Address spread out over multiple attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PartialAddressAttributeHintAttributes**](PartialAddressAttributeHintAttributes.md) |  | 

## Example

```python
from felt_api.models.partial_address_attribute_hint import PartialAddressAttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of PartialAddressAttributeHint from a JSON string
partial_address_attribute_hint_instance = PartialAddressAttributeHint.from_json(json)
# print the JSON string representation of the object
print(PartialAddressAttributeHint.to_json())

# convert the object into a dict
partial_address_attribute_hint_dict = partial_address_attribute_hint_instance.to_dict()
# create an instance of PartialAddressAttributeHint from a dict
partial_address_attribute_hint_from_dict = PartialAddressAttributeHint.from_dict(partial_address_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


