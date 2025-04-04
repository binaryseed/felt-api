# USCBSA2020AttributeHint

A hint that the data contains a US Core-based statistical area (Census 2020) attribute: https://www.census.gov/geographies/reference-maps/2020/geo/cbsa.html

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**USCBSA2020AttributeHintAttribute**](USCBSA2020AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.uscbsa2020_attribute_hint import USCBSA2020AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of USCBSA2020AttributeHint from a JSON string
uscbsa2020_attribute_hint_instance = USCBSA2020AttributeHint.from_json(json)
# print the JSON string representation of the object
print(USCBSA2020AttributeHint.to_json())

# convert the object into a dict
uscbsa2020_attribute_hint_dict = uscbsa2020_attribute_hint_instance.to_dict()
# create an instance of USCBSA2020AttributeHint from a dict
uscbsa2020_attribute_hint_from_dict = USCBSA2020AttributeHint.from_dict(uscbsa2020_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


