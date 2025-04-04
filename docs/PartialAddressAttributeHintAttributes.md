# PartialAddressAttributeHintAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | ex: USA | [optional] 
**locality** | **str** | ex: Oakland | [optional] 
**postal_code** | **str** | ex: 94612 | [optional] 
**region** | **str** | ex: California | [optional] 
**street_address** | **str** | ex: 1904 Franklin St | 

## Example

```python
from felt_api.models.partial_address_attribute_hint_attributes import PartialAddressAttributeHintAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PartialAddressAttributeHintAttributes from a JSON string
partial_address_attribute_hint_attributes_instance = PartialAddressAttributeHintAttributes.from_json(json)
# print the JSON string representation of the object
print(PartialAddressAttributeHintAttributes.to_json())

# convert the object into a dict
partial_address_attribute_hint_attributes_dict = partial_address_attribute_hint_attributes_instance.to_dict()
# create an instance of PartialAddressAttributeHintAttributes from a dict
partial_address_attribute_hint_attributes_from_dict = PartialAddressAttributeHintAttributes.from_dict(partial_address_attribute_hint_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


