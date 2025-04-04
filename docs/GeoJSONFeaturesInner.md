# GeoJSONFeaturesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**GeoJSONFeaturesInnerGeometry**](GeoJSONFeaturesInnerGeometry.md) |  | [optional] 
**properties** | **object** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from felt_api.models.geo_json_features_inner import GeoJSONFeaturesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONFeaturesInner from a JSON string
geo_json_features_inner_instance = GeoJSONFeaturesInner.from_json(json)
# print the JSON string representation of the object
print(GeoJSONFeaturesInner.to_json())

# convert the object into a dict
geo_json_features_inner_dict = geo_json_features_inner_instance.to_dict()
# create an instance of GeoJSONFeaturesInner from a dict
geo_json_features_inner_from_dict = GeoJSONFeaturesInner.from_dict(geo_json_features_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


