# EuropeanUnionNUTS22021AttributeHint

A hint that the data contains a Eurostat NUTS 2 (2021) attribute. https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**EuropeanUnionNUTS22021AttributeHintAttribute**](EuropeanUnionNUTS22021AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.european_union_nuts22021_attribute_hint import EuropeanUnionNUTS22021AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of EuropeanUnionNUTS22021AttributeHint from a JSON string
european_union_nuts22021_attribute_hint_instance = EuropeanUnionNUTS22021AttributeHint.from_json(json)
# print the JSON string representation of the object
print(EuropeanUnionNUTS22021AttributeHint.to_json())

# convert the object into a dict
european_union_nuts22021_attribute_hint_dict = european_union_nuts22021_attribute_hint_instance.to_dict()
# create an instance of EuropeanUnionNUTS22021AttributeHint from a dict
european_union_nuts22021_attribute_hint_from_dict = EuropeanUnionNUTS22021AttributeHint.from_dict(european_union_nuts22021_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


