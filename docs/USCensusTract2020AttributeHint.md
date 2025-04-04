# USCensusTract2020AttributeHint

A hint that the data contains a US Census Tract (Census 2020) attribute. https://www.census.gov/geographies/reference-maps/2020/geo/2020pl-maps/2020-census-tract.html

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**USCensusTract2020AttributeHintAttribute**](USCensusTract2020AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.us_census_tract2020_attribute_hint import USCensusTract2020AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of USCensusTract2020AttributeHint from a JSON string
us_census_tract2020_attribute_hint_instance = USCensusTract2020AttributeHint.from_json(json)
# print the JSON string representation of the object
print(USCensusTract2020AttributeHint.to_json())

# convert the object into a dict
us_census_tract2020_attribute_hint_dict = us_census_tract2020_attribute_hint_instance.to_dict()
# create an instance of USCensusTract2020AttributeHint from a dict
us_census_tract2020_attribute_hint_from_dict = USCensusTract2020AttributeHint.from_dict(us_census_tract2020_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


