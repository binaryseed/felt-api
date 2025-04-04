# LocalityAttributeHint

A hint that the data contains a Locality spread out over multiple attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**LocalityAttributeHintAttributes**](LocalityAttributeHintAttributes.md) |  | 

## Example

```python
from felt_api.models.locality_attribute_hint import LocalityAttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of LocalityAttributeHint from a JSON string
locality_attribute_hint_instance = LocalityAttributeHint.from_json(json)
# print the JSON string representation of the object
print(LocalityAttributeHint.to_json())

# convert the object into a dict
locality_attribute_hint_dict = locality_attribute_hint_instance.to_dict()
# create an instance of LocalityAttributeHint from a dict
locality_attribute_hint_from_dict = LocalityAttributeHint.from_dict(locality_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


