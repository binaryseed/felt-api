# GeoJSONFeaturesInnerGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**felt_id** | **str** |  | [optional] 
**felt_parent_id** | **str** |  | [optional] 

## Example

```python
from felt_api.models.geo_json_features_inner_geometry import GeoJSONFeaturesInnerGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONFeaturesInnerGeometry from a JSON string
geo_json_features_inner_geometry_instance = GeoJSONFeaturesInnerGeometry.from_json(json)
# print the JSON string representation of the object
print(GeoJSONFeaturesInnerGeometry.to_json())

# convert the object into a dict
geo_json_features_inner_geometry_dict = geo_json_features_inner_geometry_instance.to_dict()
# create an instance of GeoJSONFeaturesInnerGeometry from a dict
geo_json_features_inner_geometry_from_dict = GeoJSONFeaturesInnerGeometry.from_dict(geo_json_features_inner_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


