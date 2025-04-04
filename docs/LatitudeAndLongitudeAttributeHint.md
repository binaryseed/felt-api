# LatitudeAndLongitudeAttributeHint

A hint that the data contains Latitude and Longitude in two individual attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**LatitudeAndLongitudeAttributeHintAttributes**](LatitudeAndLongitudeAttributeHintAttributes.md) |  | 

## Example

```python
from felt_api.models.latitude_and_longitude_attribute_hint import LatitudeAndLongitudeAttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of LatitudeAndLongitudeAttributeHint from a JSON string
latitude_and_longitude_attribute_hint_instance = LatitudeAndLongitudeAttributeHint.from_json(json)
# print the JSON string representation of the object
print(LatitudeAndLongitudeAttributeHint.to_json())

# convert the object into a dict
latitude_and_longitude_attribute_hint_dict = latitude_and_longitude_attribute_hint_instance.to_dict()
# create an instance of LatitudeAndLongitudeAttributeHint from a dict
latitude_and_longitude_attribute_hint_from_dict = LatitudeAndLongitudeAttributeHint.from_dict(latitude_and_longitude_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


