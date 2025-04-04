# LocalityAttributeHintAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | ex: USA | [optional] 
**locality** | **str** | ex: Oakland | 
**region** | **str** | ex: California | [optional] 

## Example

```python
from felt_api.models.locality_attribute_hint_attributes import LocalityAttributeHintAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LocalityAttributeHintAttributes from a JSON string
locality_attribute_hint_attributes_instance = LocalityAttributeHintAttributes.from_json(json)
# print the JSON string representation of the object
print(LocalityAttributeHintAttributes.to_json())

# convert the object into a dict
locality_attribute_hint_attributes_dict = locality_attribute_hint_attributes_instance.to_dict()
# create an instance of LocalityAttributeHintAttributes from a dict
locality_attribute_hint_attributes_from_dict = LocalityAttributeHintAttributes.from_dict(locality_attribute_hint_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


