# LatitudeAndLongitudeCombinedAttributeHint

A hint that the data contains Latitude and Longitude combined in a single attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**LatitudeAndLongitudeCombinedAttributeHintAttribute**](LatitudeAndLongitudeCombinedAttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.latitude_and_longitude_combined_attribute_hint import LatitudeAndLongitudeCombinedAttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of LatitudeAndLongitudeCombinedAttributeHint from a JSON string
latitude_and_longitude_combined_attribute_hint_instance = LatitudeAndLongitudeCombinedAttributeHint.from_json(json)
# print the JSON string representation of the object
print(LatitudeAndLongitudeCombinedAttributeHint.to_json())

# convert the object into a dict
latitude_and_longitude_combined_attribute_hint_dict = latitude_and_longitude_combined_attribute_hint_instance.to_dict()
# create an instance of LatitudeAndLongitudeCombinedAttributeHint from a dict
latitude_and_longitude_combined_attribute_hint_from_dict = LatitudeAndLongitudeCombinedAttributeHint.from_dict(latitude_and_longitude_combined_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


