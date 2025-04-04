# EuropeanUnionLAU2021AttributeHint

A hint that the data contains a Eurostat LAU (2021) attribute. https://ec.europa.eu/eurostat/web/nuts/local-administrative-units

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**EuropeanUnionLAU2021AttributeHintAttribute**](EuropeanUnionLAU2021AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.european_union_lau2021_attribute_hint import EuropeanUnionLAU2021AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of EuropeanUnionLAU2021AttributeHint from a JSON string
european_union_lau2021_attribute_hint_instance = EuropeanUnionLAU2021AttributeHint.from_json(json)
# print the JSON string representation of the object
print(EuropeanUnionLAU2021AttributeHint.to_json())

# convert the object into a dict
european_union_lau2021_attribute_hint_dict = european_union_lau2021_attribute_hint_instance.to_dict()
# create an instance of EuropeanUnionLAU2021AttributeHint from a dict
european_union_lau2021_attribute_hint_from_dict = EuropeanUnionLAU2021AttributeHint.from_dict(european_union_lau2021_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


