# EuropeanUnionNUTS32021AttributeHint

A hint that the data contains a Eurostat NUTS 3 (2021) attribute. https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**EuropeanUnionNUTS32021AttributeHintAttribute**](EuropeanUnionNUTS32021AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.european_union_nuts32021_attribute_hint import EuropeanUnionNUTS32021AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of EuropeanUnionNUTS32021AttributeHint from a JSON string
european_union_nuts32021_attribute_hint_instance = EuropeanUnionNUTS32021AttributeHint.from_json(json)
# print the JSON string representation of the object
print(EuropeanUnionNUTS32021AttributeHint.to_json())

# convert the object into a dict
european_union_nuts32021_attribute_hint_dict = european_union_nuts32021_attribute_hint_instance.to_dict()
# create an instance of EuropeanUnionNUTS32021AttributeHint from a dict
european_union_nuts32021_attribute_hint_from_dict = EuropeanUnionNUTS32021AttributeHint.from_dict(european_union_nuts32021_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


