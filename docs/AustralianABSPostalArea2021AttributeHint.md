# AustralianABSPostalArea2021AttributeHint

A hint that the data contains a Australian ABS postal area (2021) attribute. https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/non-abs-structures/postal-areas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**AustralianABSPostalArea2021AttributeHintAttribute**](AustralianABSPostalArea2021AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.australian_abs_postal_area2021_attribute_hint import AustralianABSPostalArea2021AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of AustralianABSPostalArea2021AttributeHint from a JSON string
australian_abs_postal_area2021_attribute_hint_instance = AustralianABSPostalArea2021AttributeHint.from_json(json)
# print the JSON string representation of the object
print(AustralianABSPostalArea2021AttributeHint.to_json())

# convert the object into a dict
australian_abs_postal_area2021_attribute_hint_dict = australian_abs_postal_area2021_attribute_hint_instance.to_dict()
# create an instance of AustralianABSPostalArea2021AttributeHint from a dict
australian_abs_postal_area2021_attribute_hint_from_dict = AustralianABSPostalArea2021AttributeHint.from_dict(australian_abs_postal_area2021_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


